# MalakHacks 🎀

MalakHacks is a comprehensive toolkit designed for various cybersecurity practices and learning experiences js for Malak (but u can use it too if ur interested). This README provides an overview of its capabilities and how to set it up.

## What's Inside
1. **Installation Instructions**  
2. **Getting External Tools to Work**  
3. **How It Works**  
4. **Troubleshooting**  
5. **Disclaimer**  
6. **Credits**  

## Installation Instructions
### Installation for Termux
#### From F-Droid
1. Open F-Droid App.  
2. Search for 'MalakHacks'.  
3. Tap install.

#### From GitHub
1. Ensure Termux is installed.  
2. Execute the following commands in Termux:
   ```sh
   pkg update
   pkg install git
   git clone https://github.com/sigmakader/MalakHacks.git
   cd MalakHacks
   bash install_RI.sh
   ```

## Detailed Tool Installation Guides
### John the Ripper
1. Install dependencies:  
   ```sh
   pkg install gcc make
   ```  
2. Clone the repository:  
   ```sh
   git clone https://github.com/openwall/john.git
   ```
3. Follow the instructions in the John the Ripper repository to compile.

### Hydra
1. Install dependencies:  
   ```sh
   pkg install cmake
   ```  
2. Clone the repository:  
   ```sh
   git clone https://github.com/vanhauser-thc/thc-hydra.git
   ```
3. Follow the instructions in the Hydra repository to compile.

### Hashcat
1. Install dependencies:  
   ```sh
   pkg install opencl-clang opencl-headers
   ```
2. Clone the repository:  
   ```sh
   git clone https://github.com/hashcat/hashcat.git
   ```

### theHarvester
1. Install dependencies:  
   ```sh
   pip install theHarvester
   ```

### wafw00f
1. Install dependencies:  
   ```sh
   pip install wafw00f
   ```

### binwalk
1. Install dependencies:  
   ```sh
   pip install binwalk
   ```

### shodan
1. Install dependencies:  
   ```sh
   pip install shodan
   ```

### metasploit
1. Install dependencies:  
   ```sh
   pkg install curl git
   ```  
2. Follow the install instructions from the Metasploit GitHub page.

## Troubleshooting
- **Common Issues**:
  - Ensure all dependencies are installed as listed above.
  - If an installation fails, check your internet connection.

## Disclaimer
*I'm not responsible for anything done by Malak.*

## Credits
- Developed by [EL4Q](https://github.com/sigmakader) just for Malak, stay curious 🎀.
