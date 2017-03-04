import json

skills = []
skill = {}
skill['path'] = 'Earth Prayers'
desc = False
description = ''

with open('Earth Prayers.txt', encoding='utf-8') as f:
    for line in f:
        if line == '~\n':
            skill['path'] = 'Earth Prayers'
            skill['version'] = 3.5
            res = {}
            res['model'] = 'skilllist.skill'
            res['pk'] = len(skills)
            res['fields'] = skill
            skills.append(res)
            skill = {}
        elif line.count('"') == 2:
            desc = False
            description += line
            skill['description'] = description.replace('"', '')
            description = ''
        elif '"' in line and desc is False:
            desc = True
            description += line
        elif '"' in line and desc is True:
            desc = False
            description += line
            skill['description'] = description.replace('"', '')
            description = ''
        elif desc is True:
            description += line
        elif line == '\n':
            pass
        else:
            word = line.rstrip('\n')
            w = word.split(':')
            skill[w[0]] = w[1]

skill['path'] = 'Earth Prayers'
skill['version'] = 3.5
res = {}
res['model'] = 'skilllist.skill'
res['pk'] = len(skills)
res['fields'] = skill
skills.append(res)
skill = {}
skill['path'] = 'Scythe Mastery'
desc = False
description = ''

with open('Scythe Mastery.txt', encoding='utf-8') as f:
    for line in f:
        if line == '~\n':
            skill['path'] = 'Scythe Mastery'
            skill['version'] = 3.5
            res = {}
            res['model'] = 'skilllist.skill'
            res['pk'] = len(skills)
            res['fields'] = skill
            skills.append(res)
            skill = {}
        elif line.count('"') == 2:
            desc = False
            description += line
            skill['description'] = description.replace('"', '')
            description = ''
        elif '"' in line and desc is False:
            desc = True
            description += line
        elif '"' in line and desc is True:
            desc = False
            description += line
            skill['description'] = description.replace('"', '')
            description = ''
        elif desc is True:
            description += line
        elif line == '\n':
            pass
        else:
            word = line.rstrip('\n')
            w = word.split(':')
            skill[w[0]] = w[1]

skill['path'] = 'Scythe Mastery'
skill['version'] = 3.5
res = {}
res['model'] = 'skilllist.skill'
res['pk'] = len(skills)
res['fields'] = skill
skills.append(res)
skill = {}
skill['path'] = 'Wind Prayers'
desc = False
description = ''

with open('Wind Prayers.txt', encoding='utf-8') as f:
    for line in f:
        if line == '~\n':
            skill['path'] = 'Wind Prayers'
            skill['version'] = 3.5
            res = {}
            res['model'] = 'skilllist.skill'
            res['pk'] = len(skills)
            res['fields'] = skill
            skills.append(res)
            skill = {}
        elif line.count('"') == 2:
            desc = False
            description += line
            skill['description'] = description.replace('"', '')
            description = ''
        elif '"' in line and desc is False:
            desc = True
            description += line
        elif '"' in line and desc is True:
            desc = False
            description += line
            skill['description'] = description.replace('"', '')
            description = ''
        elif desc is True:
            description += line
        elif line == '\n':
            pass
        else:
            word = line.rstrip('\n')
            w = word.split(':')
            skill[w[0]] = w[1]

skill['path'] = 'Wind Prayers'
skill['version'] = 3.5
res = {}
res['model'] = 'skilllist.skill'
res['pk'] = len(skills)
res['fields'] = skill
skills.append(res)
skill = {}
skill['path'] = 'Unlinked Skills'
desc = False
description = ''

with open('Unlinked Skills.txt', encoding='utf-8') as f:
    for line in f:
        if line == '~\n':
            skill['path'] = 'Unlinked Skills'
            skill['version'] = 3.5
            res = {}
            res['model'] = 'skilllist.skill'
            res['pk'] = len(skills)
            res['fields'] = skill
            skills.append(res)
            skill = {}
        elif line.count('"') == 2:
            desc = False
            description += line
            skill['description'] = description.replace('"', '')
            description = ''
        elif '"' in line and desc is False:
            desc = True
            description += line
        elif '"' in line and desc is True:
            desc = False
            description += line
            skill['description'] = description.replace('"', '')
            description = ''
        elif desc is True:
            description += line
        elif line == '\n':
            pass
        else:
            word = line.rstrip('\n')
            w = word.split(':')
            skill[w[0]] = w[1]

skill['path'] = 'Unlinked Skills'
skill['version'] = 3.5
res = {}
res['model'] = 'skilllist.skill'
res['pk'] = len(skills)
res['fields'] = skill
skills.append(res)
print(json.dumps(skills))