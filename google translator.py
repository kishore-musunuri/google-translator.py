from googletrans import Translator


def translate_text(text):
    """
    Translate English text into Spanish.

    Parameters:
        text (str): English text to translate.

    Returns:
        str: Translated Spanish text.
    """
    try:
        translator = Translator()
        result = translator.translate(text, src="en", dest="es")
        return result.text

    except Exception as e:
        return f"Translation error: {e}"


def main():
    # Sample English text
    text = "Hello, how are you?"

    # Translate English to Spanish
    translated_text = translate_text(text)

    # Display the results
    print("Original Text:", text)
    print("Translated Text:", translated_text)


if __name__ == "__main__":
    main()
