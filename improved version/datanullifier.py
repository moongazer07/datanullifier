from cryptography.fernet import Fernet

 #let user chose file to encrypt
file_name = input('Enter path for file for shred: ')

for _ in range(666): # change this 7 to desired # of rounds
    fernet = Fernet(Fernet.generate_key())
    # opening the original file to encrypt
    with open(file_name, 'rb') as file:
        original = file.read()
     
    # encrypting the file
    encrypted = fernet.encrypt(original)
 
    # opening the file in write mode and
    # writing the encrypted data
    with open(file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print('File encrypted!')
    f = open(file_name, 'wb')
    f.write(b'\x74\x68\x69\x73\x20\x66\x69\x6c\x65\x20\x69\x73\x20\x6e\x6f\x77\x20\x67\x6f\x6e\x65\x20\x62\x65\x63\x61\x75\x73\x65\x20\x69\x74\x20\x77\x61\x73\x20\x64\x65\x73\x74\x72\x6f\x79\x65\x64\x20\x77\x69\x74\x68\x20\x6d\x6f\x6f\x6e\x67\x61\x7a\x65\x72\x30\x37\x27\x73\x20\x63\x72\x79\x70\x74\x6f\x73\x68\x72\x65\x64\x64\x65\x72\x20\x6c\x6f\x6c\x0a\x68\x61\x68\x61' * 1)
    f.write(b'\x30' * 1024)
    f.write(b'\x045' * 6666)
    f.write(b'\x50' * 1000)
    f.write(b'\x50' * 1000)
    f.close()
    print('File shredded!')
    print('File is destroyed!')
    print('File is gone!')
    print('File is now in the gulag of the void!')
    print('File is now unrecoverable!')
    print('File is now unreadable!')
    print('File is now devoid of meaning!')
    print('File is now devoid of purpose!')
    print('File is now devoid of information!')
    print('File is now devoid of data!')
    print('File is now devoid of anything!')
    print('the nsa now cant recover the file!')
    print('the nsa now cant read the file!')
    print('the nsa now cant understand the file!')
    print('the nsa now cant steal the file!')
    print('the nsa now cant spy on the file!')
    f = open(file_name, 'wb')
    f.write(b'\x74\x68\x69\x73\x20\x66\x69\x6c\x65\x20\x69\x73\x20\x6e\x6f\x77\x20\x67\x6f\x6e\x65\x20\x62\x65\x63\x61\x75\x73\x65\x20\x69\x74\x20\x77\x61\x73\x20\x64\x65\x73\x74\x72\x6f\x79\x65\x64\x20\x77\x69\x74\x68\x20\x6d\x6f\x6f\x6e\x67\x61\x7a\x65\x72\x30\x37\x27\x73\x20\x63\x72\x79\x70\x74\x6f\x73\x68\x72\x65\x64\x64\x65\x72\x20\x6c\x6f\x6c\x0a\x68\x61\x68\x61' * 1)
    f.write(b'\x20' * 1024)
    f.write(b'\x60' * 6666)
    f.write(b'\x50' * 1000)
    f.close()
    # ask user if they want to reboot computer to clear keys from memory
    reboot = input('Reboot computer to attempt to clear keys from memory? (y/n): ')
    if reboot == 'y':
        print('Rebooting computer...')
        import os
        os.system('reboot')
    else:
        print('Exiting program...')
        exit()