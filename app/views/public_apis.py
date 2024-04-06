# Standard Library imports

# Core Flask imports
from flask import render_template, redirect, request

# Third-party imports
import boto3
from boto3.dynamodb.conditions import Attr

# App imports


def login():
    access = request.json.get('access')
    return {
        "message": "Content found",
        "data": {'content_id': 'KONTENT'},
        "success": True
    }, 200
    return {
        "message": "Wrong user details",
        "data": None,
        "success": False
    }, 400
    dynamodb = boto3.resource('dynamodb')
    content_table = dynamodb.Table('content-test')

    scan_response = content_table.scan(
        FilterExpression=Attr('access_token').eq(access)
    )
    content = next(iter(scan_response["Items"]))
    if content:
        content_id = content["content_id"]
        return redirect(f'/upload/{content_id}', code=200)
    else:
        return {
            "message": "Wrong user details",
            "data": None,
            "error": "Auth failed"
        }, 400
