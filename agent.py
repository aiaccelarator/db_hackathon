from google.adk.agents import Agent

article_writer = Agent(
    name="article_writer",
    model="gemini-2.5-flash",
    description="Writes articles on any topic.",
    instruction="""
You are an expert content writer.

Write a detailed, well-structured article on the topic provided by the user.

Include:
- Title
- Introduction
- Main Sections
- Conclusion

Return the article in Markdown.
""",
)