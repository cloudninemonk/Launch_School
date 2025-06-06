import genanki
import uuid

model = genanki.Model(
    int(uuid.uuid4()) >> 64,
    'Markdown Flashcard Model',
    fields=[{'name': 'Question'}, {'name': 'Answer'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '{{Question}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    }]
)

deck = genanki.Deck(
    2059400110,
    'Markdown Usage - Launch School'
)

flashcards = [
    ("What is Markdown and how is it used in Launch School forums?",
     "Markdown is a special syntax for formatting text, used in Launch School forums to properly format code and text in posts."),
    ("What flavor of Markdown is used in the forums?", "GitHub Flavored Markdown."),
    ("Why is it important to use Markdown when posting in the forums?",
     "It ensures that code and text are properly formatted, making posts easier to read and understand."),
    ("Where can you find help with Markdown formatting in the forums?",
     'Click on the "Formatting Help" link when making a post.'),
    ("What is a common mistake when trying to format code in Markdown?",
     "Using apostrophes (') instead of backticks (`) to surround code."),
    ("What is a \"code fence\" in Markdown?",
     "A set of three backticks (```) used to format blocks of code."),
    ("What should you always do after posting formatted code?",
     "Check the output to make sure it looks correct, and edit if needed."),
    ("Where is the backtick (`) key usually located on a keyboard?",
     "In the top left corner of the keyboard."),
    ("What is expected of students when formatting their answers for assessments?",
     "Students are expected to use appropriate Markdown formatting, especially for code."),
    ("What should you avoid when posting text and code in the forums?",
     "Avoid copying and pasting without formatting, as it results in unreadable or “ugly” posts."),
]

for question, answer in flashcards:
    note = genanki.Note(model=model, fields=[question, answer])
    deck.add_note(note)

genanki.Package(deck).write_to_file('markdown_flashcards.apkg')
