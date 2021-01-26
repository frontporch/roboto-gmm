This is a fork of the source repository for Roboto: Google’s signature family
of fonts, the default font on Android and Chrome OS, and the
recommended font for Google’s visual language, Material Design.

It also contains the toolchain used in creating Roboto.

The font family supports all Latin, Cyrillic, and Greek characters in
Unicode 7.0, as well as the currency symbol for the Georgian lari, to
be published in Unicode 8.0.

The fonts are currently available in eighteen different styles.

[Subsetted webfonts](https://fonts.google.com/specimen/Roboto) are also available from Google Fonts.

## Setup

If you are developing on a `Windows box`, please check out the [Windows Setup](#windows-setup) before proceeding

Create a clean directory for Roboto:

```bash
mkdir -p $HOME/roboto-src
cd $HOME/roboto-src
```

Download the Roboto tools and sources:

```bash
git clone https://github.com/frontporch/roboto.git
```

Create a virtual Python environment (optional but recommended):

```bash
pip install --user virtualenv
virtualenv roboto-env
source roboto-env/bin/activate
```

Download and install the dependencies (currently requires Python 2, not 3):

```bash
cd roboto
pip install -r requirements.txt
```

#### Optional additional setup for running tests

Download the latest tarball release of HarfBuzz
[here](http://www.freedesktop.org/wiki/Software/HarfBuzz/) and extract it into
the **home** directory as `$HOME/harfbuzz` (alternatively, you can download the
latest source from GitHub via
`git clone https://github.com/behdad/harfbuzz.git`).

Build and install HarfBuzz:

```bash
cd $HOME/harfbuzz
./configure
make
sudo make install
cd $HOME/roboto-src/
```

On Ubuntu (or other distributions of GNU/Linux, using the appropriate package
manager), make sure eog is installed:

```bash
sudo apt-get install eog
```

## Run

```bash
cd roboto
make
```

## Windows Setup

You can setup this project with several different methods. There is [VirtualBox](https://www.virtualbox.org/wiki/Downloads), [Docker Container](https://www.docker.com/products/docker-hub) or you can use the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

If you choose `WSL` I recommend installing: [Ubuntu 18.04](https://www.microsoft.com/en-us/p/ubuntu-1804-lts/9n9tngvndl3q?activetab=pivot:overviewtab)

### Different methods to install with WSL

You can either install the [Roboto source](https://github.com/frontporch/roboto) on the WSL box directly or you can install it locally on the Windows box and use the `WSL Bash` in the [VSCode](https://code.visualstudio.com/download) terminal to execute the commands. 

### Potential Error: [KeyError: 'Lj'](https://github.com/googlefonts/roboto/issues/234):

You may encounter this when running `Make`. This happens when your `out` directory is case-insensitive. If the folders are on your local drive, do the following:

Open a command prompt with `administrative privileges`:

```cmd
fsutil file SetCaseSensitiveInfo [directory path] enable
```

I ended up running this command on following directories:

```console
roboto\out
roboto\out\RobotoOTF
roboto\out\RobotoUFO
roboto\out\RobotoUFO\Roboto-Thin.ufo
roboto\out\RobotoUFO\Roboto-Thin.ufo\glyphs
```

**NOTE**: Make sure the directory glyphs directory is empty when running this command
