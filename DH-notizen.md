


# Related Work

The Creativity of Text-to-Image Generation
https://dl.acm.org/doi/abs/10.1145/3569219.3569352
Untersucht die Kreativität beim Anwenden von diffusion modellen 

Can There be Art Without an Artist?
https://arxiv.org/abs/2209.07667
Untersucht den Einfluss der neuen Modelle auf die Kunstwelt und Künstler

What is in a Text-to-Image Prompt: The Potential of Stable Diffusion in Visual Arts Education <<<<<<<<<<<<<<<------------------ sehr gutes Paper
https://arxiv.org/abs/2301.01902
Untersuchung von 72000 Prompts und Formalisierung der Prompts
 - sie nutzen BERT um die named-entities zu finden (z.B. Künstlername)
 - identifizieren Teile einer Prompt und ordnen die Tokens den Teilen zu
 - Topic extraction und Zuordnung der Wörter zu Topics mit GPT-3




Generated Faces in the Wild: Quantitative Comparison of Stable Diffusion, Midjourney and DALL-E 2
https://arxiv.org/abs/2210.00586
vergleicht die verschiedenen Systeme für Gesichtgenerierung

Human Evaluation of Text-to-Image Models on a Multi-Task Benchmark
https://arxiv.org/abs/2211.12112
menschliche Bewertung der verschiedenen Modelle anhand von definierten Scenarien



https://arxiv.org/abs/2209.00796
Zusammenfassung/Überblick Diffusion Modelle


# Methoden

## Association Rules

https://medium.com/@mervetorkan/association-rules-with-python-9158974e761a

## Cooccurences

Covariance vs Correlation

Correlation ist sowas wie die normalisierte Covariance
Correlation ist im Interval -1 (beide Variablen sind perfekt/total negativ korreliert) und 1 (perfekt/total positiv korreliert)
0 bedeutet keine Correlation

https://www.mygreatlearning.com/blog/covariance-vs-correlation/


TODO Zeitfenster analysieren
(wie gross ist es?)





prompt colors analysieren
color - artist zusammenhang analysieren

Klimt hat z.B. Gold als Lieblingsfarbe

Negation analysieren (verwenden Leute "not" oder "no") --> wenn ja, weitere Analysen

Topic Modelling ueber die gesamten Prompts und dann gucken, ob unterschiedliche Kuenstler mit unterschiedlichen Topics verwendet werden.


typische Begriffe fuer Illumination einer Szene:
- sunset
- environmental windlights
- midday
- sunrise


Stilbegriffe:
- acrillic
- aquarel
- watercolor
- oil
- kanvas
- glas
- graffitti
- comic
- manga
- anime


der Zeitraum ist nur 2 Wochen
--> es folgt die Frage:
Ist der Datensatz ein Zeitraum oder ein Zeitpunkt?
Wie herausfinden? Unterscheiden sich die Daten innerhald der Zeit?
"Sind alle Tage gleich?"

-->
Analyse der Woerter mit den Kuenstlern
-->
oh Warhol, kommt ja oft fuer Comic vor



Hypothese:
werden die Namen der Top Kuenstler verwendet um die generelle QUalitaet zu erhoehen, oder weil man deren Stil moechte


-->
Aussenwahrnehmung vs Communitywahrnehmung
Top 100 Kuenstler in der echten Welt mit den Top aus dem Datensatz vergleichen


-->
most popular seed value --> seed reuse is done?


--> iterative Arbeit, User welche einen Seed explizit nutzen


--> User Analyse: Power user vs Casual user
x Prozent der User machen y Prozent der Prompts
--> Unterscheiden sich die Power User von den Casual Usern in dem Promptverhalten?
--> nutzen die Poweruser immer Greg Rutkowski oder nicht


User und Anzahl der erstellten Prompts:
89bebf4f200a853ac9a7b4dfec1edb160ade299fd60db12d0752bbfd882c6f45    224010
deleted-account                                                      93543
481f5d1579a33041518382518a5e108cfc1fea95f880d081023f533eb1afd82a     49577
5477db661bbe6ff9fd509daf812fe50af4b6216f2b296c3cbf91c6b9e528fdce     38137


Warum kommt der Seed 150 am haeufigsten vor?
die anderen Seeds sind hohe Zahlen:
print(df_large.seed.value_counts())

Seed 150 kommt jeden Tag vor


# Datasets

Künstler Excel Datensatz:
https://docs.google.com/spreadsheets/d/14xTqtuV3BuKDNhLotB_d1aFlBGnDJOY0BRXJ8-86GpA/edit#gid=0

https://huggingface.co/datasets/poloclub/diffusiondb --> 1.8 Millionen Prompts 

--> dieses nutzen wir

 

https://huggingface.co/datasets/Gustavosta/Stable-Diffusion-Prompts --> cirka 80,000 prompts 

 

https://github.com/bartman081523/stable-diffusion-discord-messages --> 1.9 Millionen vom Stable diffusion discord 


# Anderer Pandas Code:

https://github.com/geschnee/big_data/blob/main/classifier_dns_exfilt/preprocessing/extract_features.py



# Outlook Dokumente

## Expose
https://onedrive.live.com/edit.aspx?resid=DD4C24BF0899AA12!102949&ithint=file%2cdocx&authkey=!AOlqY6erJHtMzdg

## Arbeit
https://onedrive.live.com/edit.aspx?resid=DD4C24BF0899AA12!103055&ithint=file%2cdocx&authkey=!ABObQWICXRkHdc8

## Finales Dokument

https://onedrive.live.com/edit.aspx?resid=DD4C24BF0899AA12!103132&ithint=file%2cdocx&authkey=!AMsxtH2KkCtAROU