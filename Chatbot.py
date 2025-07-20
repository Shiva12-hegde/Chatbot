# aws_chatbot.py

def aws_chatbot():
    print("👋 Welcome to the AWS Course Helper Bot!")
    print("Ask me about AWS services, certification, or just say hello.")
    print("Type 'exit' to quit.\n")

    # Predefined Q&A
    responses = {
        "hi": "Hello! 👋 How can I help you with AWS today?",
        "hello": "Hi there! 😊 Ask me anything about AWS.",
        "how are you": "I’m just a bot, but I’m ready to help you! 🚀",
        "who are you": "I’m your AWS Course Helper Bot, here to guide you on AWS topics.",
        "thanks": "You’re welcome! Let me know if you have more questions.",
        "thank you": "No problem! Happy to help. 🌟",
        "bye": "Goodbye! 👋 Keep learning and exploring AWS.",
        "what is aws": "AWS (Amazon Web Services) is a cloud platform offering over 200 services like compute, storage, and databases on-demand.",
        "what is ec2": "EC2 (Elastic Compute Cloud) is a virtual server you can run in the AWS cloud.",
        "what is s3": "S3 (Simple Storage Service) is object storage to store and retrieve files anytime.",
        "what is lambda": "AWS Lambda lets you run code without provisioning servers — it's called serverless computing.",
        "how to get aws certified": "You can register for an AWS Certification exam on the AWS Training and Certification portal.",
        "what is cloudformation": "CloudFormation helps you model and provision AWS resources using templates."
    }

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'exit':
            print("🤖 Bot: Goodbye! Happy learning!")
            break

        # Look for exact match
        response = responses.get(user_input)

        if response:
            print(f"🤖 Bot: {response}\n")
        else:
            print("🤖 Bot: Sorry, I don't know that yet. Try asking about EC2, S3, Lambda, or say hi!\n")


if __name__ == "__main__":
    aws_chatbot()

