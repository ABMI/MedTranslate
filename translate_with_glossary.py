def translate_text_with_glossary(
        text,
        project_id="testtrans-1578532759135",
        glossary_id="test_glossary"
):
    global translated_output
    import google.cloud.translate_v3 as gt
    import os

    location = 'us-central1'  ## location of your gcp bucket
    credential_file = "C:/google_trans/testtrans-1578532759135-1303d7b01080.json"  ## credential key file directory
    gcs_glossary_uri = 'gs://test_med_trans/test_glossary.csv'  ## uri of storage and glossary

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_file

    client = gt.TranslationServiceClient()
    parent = client.location_path(project_id, location)

    glossary = client.glossary_path(
        project_id, location, glossary_id  # The location of the glossary
    )
    glossary_config = gt.types.TranslateTextGlossaryConfig(
        glossary=glossary)

    # Supported language codes: https://cloud.google.com/translate/docs/languages
    response = client.translate_text(
        contents=[text],
        source_language_code="ko",
        target_language_code="en",
        parent=parent,
        glossary_config=glossary_config,
    )
    for translation in response.glossary_translations:
        translated_output = translation.translated_text

    return translated_output
