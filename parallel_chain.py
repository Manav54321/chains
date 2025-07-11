from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

model = ChatGroq(
    temperature = 1,
    groq_api_key = "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",
    model_name = "meta-llama/llama-4-scout-17b-16e-instruct"
)

prompt_1 = PromptTemplate(
    template = "Generate a short and simple notes no a given text \n {text}",
    input_variables = ["text"]
)

prompt_2 = PromptTemplate(
    template = "Generate a quiz of 5 short question of yes/no on the given text \n {text}",
    input_variables = ["text"]
)

prompt_3 = PromptTemplate(
    template = "Merge the following notes and quiz into a single document \n Notes: {notes} \n Quiz: {quiz}",
    input_variables = ["notes", "quiz"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt_1 | model | parser,
    "quiz": prompt_2 | model | parser
})

chain = prompt_3 | model | parser

merged_chain = parallel_chain | chain

result = merged_chain.invoke({"text": """Caleb Zackery "Don" Toliver[2] (/ˈtɒlɪvər/ TOL-iv-ər; born June 12, 1994) is an American rapper and singer. He emerged to fame in 2018 with the release of his debut mixtape, Donny Womack, and his feature on the song "Can't Say" by fellow Houston rapper Travis Scott from the latter's third studio album Astroworld.[3] Scott also signed him to his record label, Cactus Jack Records, in a joint venture with Atlantic Records. Toliver gained more attention in mainstream music in 2019 with his single, "No Idea", and his involvement on the Cactus Jack label and Scott's compilation album, JackBoys, in which he was featured on the song "What to Do?" and had his own single, "Had Enough" (featuring Quavo and Offset).[4]

In 2020, Toliver released his debut studio album, Heaven or Hell, and also released a collaboration with Internet Money and Gunna titled "Lemonade" (featuring Nav), which peaked within the top ten of the Billboard Hot 100 and gave him his highest-charting song. Toliver released his second studio album, Life of a Don, the following year and was featured on two successful songs in late 2022: "Too Many Nights" by Metro Boomin and Future and "Used" by SZA. He released his R&B and soul-focused third studio album, Love Sick, in 2023. The following year, Toliver released his experimental trap-centered fourth studio album, Hardstone Psycho, which was led by the top-40 single "Bandit". All four of his studio albums have charted within the top ten of the Billboard 200.

Early life
Toliver was born and raised in Houston, Texas.[5][6][7] His father was a rapper during the Swishahouse movement in the early 2000s, and would commonly play music around him growing up. As a young opera singer, he was bullied because of his passion, so he pursued rap.[8]

Career
2017–2020: Commercial debut, Donny Womack, and Heaven or Hell
On December 13, 2017, Toliver released his debut single, "Diva", followed by another single titled "I Gotta" three days later.[9][10] In March 2018, he signed to Atlantic Records and fellow American rapper Chedda Da Connect's record label, We Run It Entertainment, in conjunction with Artist Partner Group. On July 6, Toliver released the single "Holdin' Steel", which features fellow American rapper Dice Soho.[11] The song serves as the lead single to his debut mixtape, Donny Womack, which was released on August 2.[12] along with a music video for the song "Diamonds".[7] The following day, fellow American rapper Travis Scott released his third studio album, Astroworld, in which Toliver was featured on the track "Can't Say".[1][13] Three days later, Scott signed Toliver to his record label, Cactus Jack.[14] On August 9, Canadian rapper Nav released the official music video for his single, "Champion", which features Scott. Toliver makes a cameo appearance in the video alongside the two artists and fellow American rappers Gunna and Sheck Wes, with the latter also being signed to Cactus Jack.[15] Later that year, Scott embarked on the first leg of his Astroworld – Wish You Were Here Tour, in which he brought Toliver out onstage at every performance to perform "Can't Say" with him, along with a few shows from the second leg the following year.

On May 29, 2019, Toliver released the single "No Idea", which eventually became a viral hit on TikTok due to many users using it as the background sound in their videos. He then released the single "Can't Feel My Legs". The two songs would serve as the respective lead and second singles from his then-upcoming debut studio album, Heaven or Hell (2020).[16] On December 27, the Cactus Jack label and Travis Scott released the compilation album JackBoys, which was named after a nickname that Scott uses to describe the artists signed to the label. Toliver was featured on the song "What to Do?" from the album and had his own single, "Had Enough", which features American rappers Quavo and Offset. He also provided additional vocals along with Scott and fellow Cactus Jack signed Luxury Tax 50 on the song "Gang Gang", which was performed by Sheck Wes. On February 21, 2020, Toliver was announced to serve as an opening act for Canadian singer the Weeknd's After Hours til Dawn Stadium Tour (called the After Hours Tour at the time), but the tour was postponed to two years later due to the COVID-19 pandemic that was going on at the time and he did not end up opening.[17] On March 13, 2020, Toliver released Heaven or Hell, in which "Had Enough" was also included. "After Party" was chosen as the fourth and final single from the album as it was sent to rhythmic contemporary radio on June 23.[18] Toliver released a collaboration with record label Internet Money and Gunna titled "Lemonade", which features Nav. The song peaked at number six on the Billboard Hot 100 later that year, giving all the artists with the exception of Gunna their highest-charting song.[19]

2021–2022: Life of a Don
On February 3, 2021, Toliver subtly tweeted the acronym "L.O.A.D", which would later be revealed to stand for his then-upcoming second studio album, Life of a Don.[20][21] He released the lead single from the album, "What You Need", on May 4.[22] He released the second single, "Drugs N Hella Melodies", which features his girlfriend, Colombian-American singer Kali Uchis, on June 18.[23] On August 20, Toliver released a collaboration with American record producer Skrillex and Canadian singer Justin Bieber titled "Don't Go".[24] On August 29, fellow American rapper Kanye West released his tenth studio album, Donda, in which Toliver was featured alongside fellow American rapper Kid Cudi on the track "Moon".[25] Toliver embarked on his first concert tour, the Life of a Don Tour, in support of the album in North America from September 18 to October 30. The album was released on October 8, with "Way Bigger" being chosen as the third single from the album on the same day.[26][27] "Flocky Flocky" (featuring Travis Scott) was chosen as the fourth and final single three days later.[28]

2022–present: Love Sick and Hardstone Psycho
On April 3, 2022, Toliver tweeted the word "LOVESICK" along with emojis of a rose and a CD, subtly hinting that his then-upcoming third studio album would be titled Love Sick.[29] On April 22, Toliver was featured alongside Lil Uzi Vert on the single "Scrape It Off" by fellow American rapper Pusha T, as part of the latter's album, It's Almost Dry. Exactly one week later, he was featured on the single "Honest" by Justin Bieber, which the two artists performed live for the latter's Justice World Tour in Houston the same day and two days later in Dallas. In an interview with GQ on September 6, Toliver described the genres of the Love Sick as "futuristic R&B and soul" and confirmed Kali Uchis would make a guest appearance on it.[30] Three days later, Nav released his fourth studio album, Demons Protected by Angels, which includes a collaboration with Toliver titled "One Time" that features fellow American rapper Future. On November 18, Toliver released the single "Do It Right", which would serve as the lead single from Love Sick.[31] On December 2, American record producer Metro Boomin released his second studio album, Heroes & Villains, in which Toliver was featured on three songs: "Too Many Nights" (with Future), "Around Me", and "I Can't Save You (Interlude)" (with Future). Exactly a week later, American singer-songwriter SZA released her second studio album, SOS, in which Toliver was featured on the track "Used". In early 2023, Toliver continued teasing Love Sick by posting a story on Instagram that shows a picture of a whiteboard with the album's title written on it.[32] He released the second single from the album, "4 Me" (featuring Kali Uchis) on February 15.[33] Two days later, he released the third single, "Leave the Club", which features fellow American rappers Lil Durk and GloRilla, and also revealed the album's release date and cover art.[34] Toliver revealed the tracklist and featured artists six days later.[35] Love Sick was released on February 24, with Toliver confirming later in the evening of that same day that a deluxe edition of the album would be released soon, along with a teaser video that played a snippet of the then-unreleased song from it titled "Embarrassed" (featuring Travis Scott), which was released four days later as one of four additional tracks. "Private Landing" (featuring Justin Bieber and Future) was chosen as the fourth single from the album as it was sent to rhythmic contemporary radio on March 14.[36] Toliver embarked on his second concert tour, the Love Sick Tour, in support of the album in North America from June 16 to July 23 and Europe from October 6 to October 22.

On February 1, 2024, Toliver released the single "Bandit" after performing it during the European leg of the Love Sick Tour and a few other performances. The same day, he took to Twitter to reveal that he would be releasing a new album soon.[37] On March 13, he revealed that it would be released in the summer that year through a post on social media, where he also secretly revealed its title.[38] The following day, he released the single "Deep in the Water", which was previously teased in the official music video of "Bandit". The two songs would serve as the respective lead and second singles from his then-upcoming fourth studio album, Hardstone Psycho. On March 17, while performing at the hip hop music festival Rolling Loud at the SoFi Stadium in Inglewood, California, he confirmed the title of the album before performing the then-unreleased song from it titled "Tore Up" for the first time.[39] On May 22, Toliver released the third and final single of the album, "Attitude", which features fellow American singer Charlie Wilson and fellow American rapper and record producer Cash Cobain, and also revealed its release date.[40] He revealed its tracklist on June 12, 2024, which was his 30th birthday.[41] Hardstone Psycho was released on June 14. Eleven days later, he hinted at a possible collaborative studio album with Travis Scott in an interview with GQ.[42] On August 3, Kanye West and Ty Dolla Sign surprise-released their second studio album under the super duo ¥$ titled Vultures 2, which includes a collaboration with Toliver and Playboi Carti titled "Field Trip" that features Kodak Black. Toliver embarked on his third concert tour, the Psycho Tour, in support of Hardstone Psycho in North America from October 12 to November 21.

On February 9, 2025, SZA released four additional songs from her reissued studio album, Lana (2024), in which Toliver was featured on the track "Joni". Three days later, "No Pole", which appears on the deluxe edition of Toliver's previous album, Love Sick, was chosen as the fifth and final single from the album as it was sent to rhythmic contemporary radio.[43] The song became popular through TikTok in late 2024 and entered numerous music charts after not charting anywhere for almost two years since its release. On February 21, Toliver released a collaboration with his Louis Vuitton bag that he named "Speedy" and credited as an artist on the song and South Korean rapper J-Hope titled "LV Bag", which features American musician Pharrell Williams.[44] On April 30, he released the single "Lose My Mind" (featuring Doja Cat), which serves as the lead single from the soundtrack album of the film F1.[45] Toliver continued the Psycho Tour in Europe from May 13 to June 13. He released the single "FWU" on June 27.[46] Sometime the next month, the Cactus Jack label and Travis Scott are set to release the compilation album JackBoys 2, a sequel to their 2019 album.[47]

Personal life
He has been dating American singer Kali Uchis since 2020.[48] In January 2024, he announced he was expecting his first child with Uchis; two months later, they celebrated the birth of their son.[49][50] On March 14, Toliver released the song "Deep in the Water" alongside a music video, which was dedicated to Uchis and their son.[51]

In April 2024, Toliver was pulled over by highway patrol in San Fernando Valley, California for speeding and DUI; he was not taken to jail and was instead cited and released into the custody of the vehicle's passenger.[52]

Discography
Main article: Don Toliver discography
Studio albums

Heaven or Hell (2020)
Life of a Don (2021)
Love Sick (2023)
Hardstone Psycho (2024)
Concert tours
Headlining

Life of a Don Tour (2021)
Love Sick Tour (2023)
Psycho Tour (2024)
Supporting

Future - One Big Party Tour (2023)
"""})

print(result)

merged_chain.get_graph().print_ascii()
# LCEL = langchain expression language