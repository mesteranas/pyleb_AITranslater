from .. import exceptions
import google.generativeai as genai
class Gemini:
    def __init__(self,apiKey:str):
        """
        this class makes you to translate or summarize any text using gemini rebot from google
        :param apiKey: The API key for authentication to get it visite "https://makersuite.google.com/app/apikey"
        :type apiKey: str
        """
        self.apiKey = apiKey
        genai.configure(api_key=self.apiKey)
        self.model = genai.GenerativeModel()
    def translate(self,text:str,translateTo:str):
        """
        this function translate the givven text into the select text using gemini
        :param text: the text to translate
        :type text: str
        :param translateTo: the language you wish to translate into . you can checkout the supported languages list for more information
        :type translateTo: str
        """
        prompt=f"""translate: 
        {text}
        to {translateTo}
        give me the translated text only don't type any things except the text"""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except:
            raise exceptions.TranslationError()
    def summarizeAndTranslate(self,text:str,translateTo:str):
        """
        this function summarize and translate the givven text into the select language using gemini
        :param text: the text to summarize
        :type text: str
        :param translateTo: the language you wish to translate into . you can checkout the supported languages list for more information
        :type translateTo: str
        """
        prompt = f"""
Summarize the following text and translate the summary into {translateTo}:
Text:
{text}

Please provide only the summarized text in the specified language. Ensure the summary is concise and captures the main points accurately.
and don't type any thing in the message except the text
"""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except:
            raise exceptions.TranslationError()