### Hi there 👋

<!--
**shimadakambei125/shimadakambei125** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

# My name is **Bibz**!
## I am an apsiring software developer but currently working in the field of Healthcare
![This is an image of a copueter from unsplash.com](https://images.unsplash.com/photo-1471897488648-5eae4ac6686b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80)

<sup>This picture is from www.unsplash.com</sup>
###### My Journey started the last few months when Python got my attention.
###### I have always have fascination with computer and programming and I have decided to take a step forward.
###### I have joined a bootcamp recently for software engineering with Python as my main programming language.
###### So far so good! 😄  The best part is that I still code after a 13 hour busy shift in A&E!
**⚡This means that I have found my **passion**!⚡
###### I am a keen and a fast learnerand I am a teamplayer!
###### The discipline and the soft skills I have gained in my curent profession will definitely help me
### In my new found journey as a Programmer!


<sub>Message me on Linkedin >>> https://www.linkedin.com/in/bibiano-john-aranda-a9799a24b/ </sub>

### My other hobbies
-Photography
*Beatboxing
+Cooking

## Patient Flow Modeller

This repository includes a small application called **Patient Flow Modeller**. The tool reads a CSV file describing the movement of patients through different areas of the department and displays them on a simple map.

### Usage

```
python3 main.py <path_to_csv>
```

To run in a non-graphical environment (useful for quick tests) use:

```
python3 main.py <path_to_csv> --no-gui
```

### CSV Format

The CSV file should have a header followed by rows with the following columns:

1. `patient_id`
2. `arrival_time` (ISO format: `YYYY-MM-DDTHH:MM:SS`)
3. pairs of `location` and `time` columns for each move
4. `departure_time`

Example:

```
patient_id,arrival_time,location1,time1,location2,time2,departure_time
1,2023-07-24T09:00:00,RATS,2023-07-24T09:10:00,RESUS,2023-07-24T09:40:00,2023-07-24T10:00:00
```

Running the script without `--no-gui` opens a window dividing the map into the following areas: **RATS**, **RESUS**, **MAJORS**, **ACA**, **CHILDREN'S ED** and **UTC**. Each patient is drawn as a small blue circle in the correct area.

