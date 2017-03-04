import re, string, json;

skills = []
skill = {}
skill['Path'] = 'Earth Prayers'
desc = False
description = ''

with open('Earth Prayers.txt', encoding='utf-8') as f:
    for line in f:
        if line == '~\n':
        	skill['Path'] = 'Earth Prayers'
        	skills.append(skill)
        	skill = {}
        elif line.count('"') == 2:
        	desc = False
        	description += line
        	skill['Description'] = description.replace('"', '')
        	description = ''
        elif '"' in line and desc == False:
        	desc = True
        	description += line
        elif '"' in line and desc == True:
        	desc = False
        	description += line
        	skill['Description'] = description.replace('"', '')
        	description = ''
        elif desc == True:
        	description += line
        elif line == '\n':
        	pass
        else:
        	word = line.rstrip('\n')
        	w = word.split(':')
        	skill[w[0]] = w[1]

skill = {}
skill['Path'] = 'Scythe Mastery'
desc = False
description = ''

with open('Scythe Mastery.txt', encoding='utf-8') as f:
    for line in f:
        if line == '~\n':
        	skill['Path'] = 'Scythe Mastery'
        	skills.append(skill)
        	skill = {}
        elif line.count('"') == 2:
        	desc = False
        	description += line
        	skill['Description'] = description.replace('"', '')
        	description = ''
        elif '"' in line and desc == False:
        	desc = True
        	description += line
        elif '"' in line and desc == True:
        	desc = False
        	description += line
        	skill['Description'] = description.replace('"', '')
        	description = ''
        elif desc == True:
        	description += line
        elif line == '\n':
        	pass
        else:
            word = line.rstrip('\n')
            w = word.split(':')
            skill[w[0]] = w[1]

skill = {}
skill['Path'] = 'Wind Prayers'
desc = False
description = ''

with open('Wind Prayers.txt', encoding='utf-8') as f:
    for line in f:
        if line == '~\n':
            skill['Path'] = 'Wind Prayers'
            skills.append(skill)
            skill = {}
        elif line.count('"') == 2:
        	desc = False
        	description += line
        	skill['Description'] = description.replace('"', '')
        	description = ''
        elif '"' in line and desc == False:
        	desc = True
        	description += line
        elif '"' in line and desc == True:
        	desc = False
        	description += line
        	skill['Description'] = description.replace('"', '')
        	description = ''
        elif desc == True:
        	description += line
        elif line == '\n':
        	pass
        else:
        	word = line.rstrip('\n')
        	w = word.split(':')
        	skill[w[0]] = w[1]

skill = {}
skill['Path'] = 'Unlinked Skills'
desc = False
description = ''

with open('Unlinked Skills.txt', encoding='utf-8') as f:
    for line in f:
        if line == '~\n':
            skill['Path'] = 'Unlinked Skills'
            skills.append(skill)
            skill = {}
        elif line.count('"') == 2:
        	desc = False
        	description += line
        	skill['Description'] = description.replace('"', '')
        	description = ''
        elif '"' in line and desc == False:
        	desc = True
        	description += line
        elif '"' in line and desc == True:
        	desc = False
        	description += line
        	skill['Description'] = description.replace('"', '')
        	description = ''
        elif desc == True:
        	description += line
        elif line == '\n':
        	pass
        else:
            word = line.rstrip('\n')
            w = word.split(':')
            skill[w[0]] = w[1]

print(json.dumps(skills))