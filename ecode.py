import art
print(art.logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
   
    for letter in original_text:
        if letter not in alphabet:
            output_text+=letter
        else:
            if encode_or_decode=="encode":
                 shifted_position = alphabet.index(letter) + shift_amount
            elif encode_or_decode=="decode":
                 shifted_position = alphabet.index(letter) + shift_amount
            else:
                  
                print("Invalid option. Use 'encode' or 'decode'.")
                return
               


           
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?
should_continue=True
while should_continue==True:

    ques = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    msg = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_msg=msg, shift_amount=shift, encode_or_decode=ques)
    restart=input("Type 'yes' if you want to go again. Otherwise, type 'no'\n.").lower()
    if restart=='no':
        should_continue=False
        print("goodbye")



