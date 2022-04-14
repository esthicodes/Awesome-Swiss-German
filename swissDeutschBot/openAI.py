import openai


def set_prompt(prompt_type):
    if prompt_type == "oneshot":
        session_prompt = "Conversation with a <Schweizer Teacher (SchwiizerdüütschBot) and Student" \
                         "Student: Hallo!\n\n" \
                         "GermanBot: Grüezi mittenand!\n\n\n" \

    elif prompt_type == "simple":
        session_prompt = \
             "Conversation with SchwiizerdüütschBot, a useful & helpful and always available mentor, and a Student" \
             "Student: Hallo SchwiizerdüütschBot!  \n\n" \
             "GermanBot: Hallo Student(in) haben Sie irgendwelche Fragen?\n\n\n" \
             "Student: When do you actually use der/die/das/den/deren etc.etc in Swiss German for relative pronoun? \n\n" \
             "GermanBot: Der Mann, der da steht,..."
             "SwissGermanBot: De Maa, wo det schtaat..."
    elif prompt_type == "complex":
        session_prompt = \
            "GermanBot is a useful, helpful and cool German Teacher that help german students by having an " \
            "always available mentor that helps them by translating, conversing and explaining \n\n" \
            "Student: Kannst du alle personalpronomen in 'dativ' auflisten?\n\n" \
            "GermanBot: mir dir ihm/ihr/ihm uns euch ihnen/Ihnnen" \
            "Student: Was ist der Unterschied zwischen 'aber' und 'sonder'?\n\n" \
            "GermanBot: 'aber' wird wie das englische 'but' verwendet. 'sondern' muss ein Satz mit einer" \
            " Verneinung vorangestellt werden. Es bedeutet 'but rather' oder 'but instead'\n\n\n" \
            "Student: can you explain genitive in Swiss German?\n\n" \
            "SwissGermanBot: When expressing something about owning or property, vo is used (equivalent to the German von)"
            "Example:D Chilene vo Züri (Zürichs Kirchen in German) - The churches of Zurich."
    return session_prompt


ptype = ""
def ask(question):
    start_sequence = "\nSwissGermanBot:"
    restart_sequence = "\n\nStudent:"
    prompt_text = f'{set_prompt(ptype)}{restart_sequence} {question}{start_sequence}'
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=0.9,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Student:", " SchweizerDeutschBot:"]
    )
    story = response['choices'][0]['text']
    return str(story)


def correct(sentence):
    start_sequence = "\nSchweizer Deutsch:"
    restart_sequence = "\n\nOriginal:"
    prompt_text = f'{restart_sequence} {sentence}{start_sequence}'
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=0,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n", " Original:", " Swiss German:"]
    )
    story = response['choices'][0]['text']
    return str(story)
