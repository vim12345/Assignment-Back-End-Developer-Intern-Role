from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for comments (replace with actual API call)
comments_data = [
    {
        "at": "01-01-2023",
        "author": "Fredrick Johnson",
        "like": 3,
        "reply": 2,
        "text": "Economic growth is important."
    },
    {
        "at": "01-02-2023",
        "author": "John Doe",
        "like": 7,
        "reply": 1,
        "text": "I agree with Fredrick."
    },
    # Add more comment data here
]

@app.route('/search', methods=['GET'])
def search_comments():
    search_author = request.args.get('search_author')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    like_from = request.args.get('like_from')
    like_to = request.args.get('like_to')
    reply_from = request.args.get('reply_from')
    reply_to = request.args.get('reply_to')
    search_text = request.args.get('search_text')

    # Filter comments based on search criteria
    filtered_comments = []
    for comment in comments_data:
        if (not search_author or search_author.lower() in comment['author'].lower()) and \
           (not at_from or comment['at'] >= at_from) and \
           (not at_to or comment['at'] <= at_to) and \
           (not like_from or comment['like'] >= int(like_from)) and \
           (not like_to or comment['like'] <= int(like_to)) and \
           (not reply_from or comment['reply'] >= int(reply_from)) and \
           (not reply_to or comment['reply'] <= int(reply_to)) and \
           (not search_text or search_text.lower() in comment['text'].lower()):
            filtered_comments.append(comment)

    return jsonify(filtered_comments)

if __name__ == '__main__':
    app.run(debug=True)
