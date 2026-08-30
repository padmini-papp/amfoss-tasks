# Task 1

## Level 1: Among the four sectors, all the devil fruits files have similar names and description, so just using cat on each of them doesn't help.

At first I ran ls -la inside each sectors and noticed that almost all files had the same permission rw-r--r-- except one file in sector_c, devil_fruit_6.txt which has the permission rwxr-xr-x and also showed up in green in the terminal, since executable files are color coded differently.

I figured this was the real one since the readme said the genuine fruit still has "the power to awaken itself", meaning it can actually be run/executed, unlike the fake ones which are just locked files.

Ran:
./eat.sh sector_C/devil_fruit_6.txt

Got the flag:
ONE_PIECE{GITO_GITO_NO_AWAKENING}

If I had picked the wrong file it just would've said nothing happened.

---

## Level 2: feast_manifest.txt in the main folder was a red herring, just some random food items listed, didn't lead anywhere.

Ran git branch -a and found a hidden branch called whiskey_peak_investigation that wasn't visible on the normal branch. Checked it out using git checkout whiskey_peak_investigation.

That revealed a hidden folder called .baroque_works_cache (it's a dotfile so it doesn't show up unless you use ls -la). Inside was a script called unlock_vault.sh.

Read it with cat before running it since you shouldn't run scripts blindly. The script checks an environment variable called AWAKENING_SIGNATURE (my level 1 flag), hashes it using sha256sum and compares it against a hardcoded hash value inside the script. Hashing basically turns any text into a fixed scrambled fingerprint, and you can't reverse it back, so this is how the script verifies I had the right flag without storing it in plain text.

If the hash matches, it decrypts a flag using openssl (which is actual reversible encryption, different from hashing) using my flag as the password, and writes the decrypted flag into line 42 of a log file.

Had to set the variable first since env variables only exist for the current terminal session:
export AWAKENING_SIGNATURE=ONE_PIECE_GITO_GITO_NO_AWAKENING

Ran the script and got a sed error. Turns out on Mac, sed -i needs an extra empty argument right after it that Linux doesn't need, since Mac uses a different version of sed (BSD sed vs GNU sed on Linux). Fixed the line inside the script to add the empty quotes after -i.

Ran it again, worked with no errors, and it dropped two log files that were supposed to be identical except for the flag. Used diff to compare them line by line instead of checking manually:
diff marine_intercept.log bounty_hunter_feed.log

Found the difference on line 42:
BAROQUE_DIAL_SPLIT_TIMELINE_MISDIRECTION

---

## Level 3: Wax_Jungle folder on the main branch only had an empty file called .gitkeep, so nothing useful there.

Checked git branch -a again since the same trick worked in level 2, and found another hidden branch called little_garden, which actually matches this level's real name in the readme story.

Checked it out and found a bunch of nested folders with hundreds of report log files scattered everywhere, all saying generic stuff like SYSTEM_DUMP FALSE ALARM or SYSTEM_DUMP NO RECORDS FOUND. Since they all looked the same, instead of trying to guess or manually check every file, I searched for the one file that DIDN'T follow that same pattern:
grep -rL SYSTEM_DUMP .

grep -r searches recursively through all subfolders, and -L is the opposite of a normal search, it lists files that do
