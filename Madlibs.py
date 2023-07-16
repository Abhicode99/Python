def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input


noun = get_input("noun")
adjective1 = get_input("adjective")
adjective2 = get_input("adjective")
past_verb1 = get_input("past tense verb")
number1 = get_input("number")
adverb1 = get_input("adverb")

story = f"""
Today, my fabulous camp group went to a 
{adjective1} amusement park. It was a fun park with lots of cool {noun}
and enjoyable play structures. When we got there, my kind counselor shouted loudly, 
"Everybody off the {noun}." We all pushed out in a terrible hurry. My counselor handed out 
yellow tickets, and we scurried in. I was so excited! I couldn't figure out
what exciting thing to do first. I saw a scary roller coaster I really liked so, I {adverb1} ran
over to get in the long line that had about {number1} people in it. When I finally
got on the roller coaster I was {past_verb1}. In fact I was so nervous my two knees
were knocking together. This was the {adjective2} ride I had ever been on! In about two
minutes I heard the crank and grinding of the gears. That’s when the ride began! When I got to
the bottom, I was a little {past_verb1} but I was proud of myself. The rest of the day went
{adverb1}. It was  {adjective2} day at the fun park. 
"""

print(story)