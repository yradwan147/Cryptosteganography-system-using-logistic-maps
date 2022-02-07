# Cryptosteganography system using logistic maps

## Methodology

1. For each pixel in the input photo, there exists 3 main channels (R,G,B) which all consist of one 8 bit value. For each bit in the red value we hide it in 8 corresponding bytes in the holder photo where the bit is placed in the least significant bit. This process is replicated for the 2 other channels. This is our implementation of steganography
2. To further encrypt the image, we used a logistic map function with starter values of lamba = 4 and x_node = 0.2 to generate chaotic random values for our encryption
3. For each pixel in our input photo, we generate 3 values from our logistic function. The last 2 bits of these 3 values are then combined using XOR to generate 2 bits which are used for our multiplexer operation to scramble the order of the pixel values in the pixel (i.e G,B,R instead of R,G,B)
4. Finally, the 3 channel values per pixel are also encrypted by doing an XOR operation between them and the last 8 bits of the 3 logistic values. Thus the final resulting pixel is scrambled and encrypted.
5. This image is then hidden using the previous methodology. Decryption is run by reversing the previous steps using the 3 same 3 logistic values per pixel.
6. Our system was evaluated using renowned scoring systems for encryption including pixel correlation constants, entropy, differential attack measures, and sensitivity to change in one bit.

## References

• Gómez, E. H. J. M. A. (2020, June 6). Implementation of a Crypto-Steganographic System Based on the AES-CBC Algorithm | International Journal of Advanced Science and Technology. SERSC. http://sersc.org/journals/index.php/IJAST/article/view/30631
• Radwan, A. G., AbdElHaleem, S. H., & Abd-El-Hafiz, S. K. (2016, March 1). Symmetric encryption algorithms using chaotic and non-chaotic generators: A review. ScienceDirect. https://www.sciencedirect.com/science/article/pii/S2090123215000752
• Rahmani, M. K. I. (2014, October 31). A Crypto-Steganography: A Survey. The Science and Information Organization. https://thesai.org/Publications/ViewPaper?Volume=5&Issue=7&Code=IJACSA&SerialNo=22
