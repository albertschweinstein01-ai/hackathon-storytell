import streamlit as st
def charactercard():
    CHAMPIONS = [
        {
            "name": "Diana",
            "title": "The Moonlight Archer",
            "lore": "A kindhearted archer blessed by the moonlight to protector the downtrodden.",
            "image": "https://universe-meeps.leagueoflegends.com/v1/assets/characters/diana-c38d12bc5446bbaa9ebf144d5fd7664682080afb9a2401f7a7c4506412993fc8.jpg"
        },
        {
            "name": "Yasuo",
            "title": "The Unforgiven",
            "lore": "An Ionian swordsman on a quest for redemption.", 
            "image": "https://universe-meeps.leagueoflegends.com/v1/assets/characters/yasuo-def7357b9742fdb66fa1bf72d41cbd5b879728fea6aca44c068c3bda19eb7d74.jpg"
        }  
    ]

    STORY = [
        {
            "name": "Your Story",
            "summary": "This is the summary of the current story and its events",
            "location": "The Ancient Kingdom Aldezar"
        }
    ]

    def character_card(champion):
        st.header(champion['name'])
        st.subheader(champion['title'])
        st.write(champion['lore'])

    def story_card(story):
        st.header(story['name'])
        st.write(story['summary'])
        st.write(story['location'])

    with st.sidebar:
        selected_champs = st.multiselect('Choose champions', options=[c['name'] for c in CHAMPIONS])

        for i, champ in enumerate(CHAMPIONS):
            if champ['name'] in selected_champs: 
                character_card(champ)

        st.divider()

        story_card(STORY[0])