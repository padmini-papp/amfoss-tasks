# Task 1

**Level 1** - among the four sectors, all the devil fruit files have similar names and descriptions, so just using cat on each of them doesn't help

At first I ran ls -la inside each sector and noticed that almost all files had the same permission rw-r--r-- except one file in sector_c, devil_fruit_6.txt, which had rwxr-xr-x and also showed up in green in the terminal since executable files are color coded differently

I figured this was the real one since the readme said the genuine fruit still has the power to awaken itself, meaning it can actually be run, unlike the fake ones which are just locked files

Ran ./eat.sh sector_C/devil_fruit_6.txt and got the flag ONE_PIECE{GITO_GITO_NO_AWAKENING}. If I had picked the wrong file it just would've said nothing happened

<br>

**Level 2** - feast_manifest.txt in the main folder was a red herring, just some random food items listed that didn't lead anywhere

Running git branch -a revealed a hidden branch called whiskey_peak_investigation that wasn't visible on the normal branch. Checking it out revealed a hidden folder called .baroque_works_cache, which doesn't show up unless you use ls -la since it's a dotfile. Inside was a script called unlock_vault.sh

I read it with cat before running it since you shouldn't run scripts blindly. It checks an environment variable called AWAKENING_SIGNATURE, my level 1 flag, hashes it with sha256sum, and compares it against a hardcoded hash. If it matches, it decrypts a flag using openssl with my flag as the password, and writes the decrypted flag into line 42 of a log file

I had to export the variable first since environment variables only exist for the current terminal session. Running the script gave a sed error at first, turns out on Mac, sed -i needs an extra empty argument that Linux doesn't need, since Mac uses a different version of sed. After fixing that inside the script it ran cleanly and dropped two log files. Using diff to compare them line by line, I found the difference on line 42: BAROQUE_DIAL{SPLIT_TIMELINE_MISDIRECTION}

<br>

**Level 3** - Wax_Jungle on the main branch only had an empty .gitkeep file. Checking git branch -a again revealed another hidden branch, little_garden, matching this level's real name in the story

Checking it out revealed a bunch of nested folders full of report log files, all saying generic things like SYSTEM_DUMP FALSE ALARM. Instead of checking each one manually I searched for the file that didn't match that pattern using grep -rL SYSTEM_DUMP, which searches recursively and lists files that do not contain the given text

That found agent_manifest.log buried deep in a nested folder, which had a SECURITY_TAG in base64 that decoded back into my level 2 flag, confirming it was genuine, along with PONEGLYPH_FRAGMENT_I, saved for later

<br>

**Level 4** - found one file, puffing_tom_blueprints, with no extension at all. Cat showed garbled binary text but one readable string stood out, step2_blueprints.tar

Using the file command instead of guessing from the name confirmed it was gzip compressed data. After renaming and extracting it I got a zip file, extracted that too, and found secret_link.txt containing PONEGLYPH_FRAGMENT_II, and frame_specs.dat, which was genuine plain text but just a decoy message

No traditional flag this level, the reward was the second fragment

<br>

**Level 5** - no Enies_Lobby folder existed on the main branch. Checking git log with stat showed nothing useful either

I remembered a third unexplored branch from earlier, alternate_timeline, which matched the story's another version of history theme. Checking it out revealed Enies_Lobby, containing a decoy script and a Python script that decodes a base64 encoded, XOR scrambled input

Combining my two saved fragments and feeding them in gave back a URL to another GitHub repo instead of a normal flag

<br>

**Level 6** - cloned the new repo and found a branch called pirate_king_path alongside the current ancient_history. Merging it in caused real conflicts in two files, both showing two half words that needed combining

I edited both manually with nano, removed the conflict markers, joined the half words correctly, and committed the resolution. Running the included victory script and entering the combined password gave the final flag, confirming everything was correct
