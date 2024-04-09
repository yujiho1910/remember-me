# Standard Library imports
import requests

# Core Flask imports
from flask import render_template, redirect, request

# Third-party imports
import boto3
from boto3.dynamodb.conditions import Attr

# App imports


def login():
    access = request.json.get("access")

    dynamodb = boto3.resource("dynamodb", region_name="ap-southeast-1")
    content_table = dynamodb.Table("content-test")

    scan_response = content_table.scan(FilterExpression=Attr("access_token").eq(access))

    if scan_response["Items"]:
        content = next(iter(scan_response["Items"]))
        content_id = content["content_id"]

        return {
            "message": "Content found",
            "data": {"content_id": content_id},
            "success": True,
        }, 200
    else:
        return {"message": "Wrong user details", "data": None, "success": False}, 400


def contact():
    payload = request.json.get("body")

    # initiate the call to lambda function
    response = requests.post(
        "https://2kt2uoqbhdcp2cvbw7jvl5i65y0rggdi.lambda-url.ap-southeast-1.on.aws/",
        json=payload,
    )

    if response.status_code == 200:
        return {
            "message": "Account creation successful",
            "data": {
                "access_token": response.json()["access_token"],
            },
            "success": True,
        }, 200
    else:
        return {
            "message": "Account creation failed",
            "data": None,
            "success": False,
        }, 400
