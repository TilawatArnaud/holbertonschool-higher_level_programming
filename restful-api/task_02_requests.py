#!/usr/bin/python3
"""
Module for fetching posts from JSONPlaceholder API.

This module provides functions to fetch posts from the JSONPlaceholder API
and either print them or save them to a CSV file.

Functions:
    fetch_and_print_posts(): Fetches posts and prints their titles.
    fetch_and_save_posts(): Fetches posts and saves them to a CSV file.
"""

import requests
import json
import csv


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder API and prints their titles.
    This function makes a GET request to the API to fetch all posts.
    If successful, it prints each post's title.
    The status code is also printed.

    Returns:
        None
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder API and saves them to a CSV file.

    This function makes a GET request to the API to fetch all posts.
    If successful, it saves the posts to 'posts.csv'
    with columns for id, title, and body.
    The file is created in the current directory.

    Returns:
        None
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        post_data = []
        for post in posts:
            post_data.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })

        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(post_data)

        print(f"Successfully saved {len(post_data)} posts to posts.csv")
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")
