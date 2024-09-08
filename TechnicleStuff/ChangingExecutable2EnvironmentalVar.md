To run `ssrfmap.py` by simply typing `ssrfmap`, you can create an alias or make the script executable and add it to your system's `$PATH`. Here's how to do it:

### Step 1: Make the Script Executable

First, make sure `ssrfmap.py` is executable. Run this command:

```bash
chmod +x /home/bc-here/SSRFmap/ssrfmap.py
```

### Step 2: Create a Symlink or Add to Your PATH

#### Option 1: Create a Symlink

You can create a symbolic link to the script in a directory that's already in your `$PATH`, such as `/usr/local/bin`:

```bash
sudo ln -s /home/bc-here/SSRFmap/ssrfmap.py /usr/local/bin/ssrfmap
```

#### Option 2: Add the Directory to `$PATH`

Alternatively, you can add the `SSRFmap` directory to your `$PATH` by editing your `.zshrc`:

```bash
nano ~/.zshrc
```

Add this line:

```bash
export PATH="$PATH:/home/bc-here/SSRFmap"
```

Save and exit, then apply the changes:

```bash
source ~/.zshrc
```

### Step 3: Run the Script

Now, you should be able to run the script by simply typing `ssrfmap` from anywhere in the terminal:

```bash
ssrfmap
```

This will execute the `ssrfmap.py` script without needing to specify `python3`.
