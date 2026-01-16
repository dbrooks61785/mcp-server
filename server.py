#!/usr/bin/env python3
"""
Simple MCP Server Example
A basic Model Context Protocol server that provides a "hello" tool.
"""

import asyncio
import json
from typing import Any
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import os
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle

# Create server instance
# Gmail authentication
SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    """Authenticate and return Gmail API service."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Note: For production, credentials.json must be provided
            if os.path.exists('credentials.json'):
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            else:
                raise Exception("credentials.json not found. Please set up Google OAuth credentials.")
        
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return build('gmail', 'v1', credentials=creds)


app = Server("hello-world-server")

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="hello",
            description="A simple tool that returns a greeting message",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Name of the person to greet"
                    }
                },
                "required": ["name"]
            }
        ),
                Tool(
            name="send_email",
            description="Send an email via Gmail",
            inputSchema={
                "type": "object",
                "properties": {
                    "to": {
                        "type": "string",
                        "description": "Recipient email address"
                    },
                    "subject": {
                        "type": "string",
                        "description": "Email subject"
                    },
                    "body": {
                        "type": "string",
                        "description": "Email body content"
                    }
                },
                "required": ["to", "subject", "body"]
            }
        ),
        Tool(
            name="read_emails",
            description="Read recent emails from Gmail inbox",
            inputSchema={
                "type": "object",
                "properties": {
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of emails to retrieve (default: 10)",
                        "default": 10
                    }
                }
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool calls."""
    if name == "hello":
        person_name = arguments.get("name", "World")
        greeting = f"Hello, {person_name}! Welcome to the MCP server."
        return [
            TextContent(
                type="text",
                text=greeting
            )
        ]
            elif name == "send_email":
        try:
            service = get_gmail_service()
            to = arguments.get("to")
            subject = arguments.get("subject")
            body = arguments.get("body")
            
            message = MIMEText(body)
            message['to'] = to
            message['subject'] = subject
            
            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            send_message = service.users().messages().send(
                userId="me",
                body={'raw': raw_message}
            ).execute()
            
            return [
                TextContent(
                    type="text",
                    text=f"Email sent successfully to {to} with subject: {subject}"
                )
            ]
        except Exception as e:
            return [
                TextContent(
                    type="text",
                    text=f"Error sending email: {str(e)}"
                )
            ]
    
    elif name == "read_emails":
        try:
            service = get_gmail_service()
            max_results = arguments.get("max_results", 10)
            
            results = service.users().messages().list(
                userId="me",
                maxResults=max_results
            ).execute()
            messages = results.get('messages', [])
            
            if not messages:
                return [
                    TextContent(
                        type="text",
                        text="No messages found in inbox."
                    )
                ]
            
            email_list = []
            for msg in messages:
                message = service.users().messages().get(
                    userId="me",
                    id=msg['id'],
                    format='metadata',
                    metadataHeaders=['From', 'Subject', 'Date']
                ).execute()
                
                headers = message.get('payload', {}).get('headers', [])
                from_header = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
                subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
                date = next((h['value'] for h in headers if h['name'] == 'Date'), 'Unknown Date')
                
                email_list.append(f"From: {from_header}\nSubject: {subject}\nDate: {date}\n")
            
            return [
                TextContent(
                    type="text",
                    text="\n---\n".join(email_list)
                )
            ]
        except Exception as e:
            return [
                TextContent(
                    type="text",
                    text=f"Error reading emails: {str(e)}"
                )
            ]
    else:
        raise ValueError(f"Unknown tool: {name}")

async def main():
    """Run the server."""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
