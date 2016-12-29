import sys
import chilkat

key = chilkat.CkSshKey()

#  Load an unencrypted or encrypted PuTTY private key.

#  If  your PuTTY private key is encrypted, set the Password
#  property before calling FromPuttyPrivateKey.
#  If your PuTTY private key is not encrypted, it makes no diffference
#  if Password is set or not set.
#key.put_Password("secret")

#  First load the .ppk file into a string:

keyStr = key.loadText("rsa_sftpkey.ppk")

#  Import into the SSH key object:
success = key.FromPuttyPrivateKey(keyStr)
if (success != True):
    print(key.lastErrorText())
    sys.exit()

#  Convert to an encrypted or unencrypted OpenSSH key.

#  First demonstrate converting to an unencrypted OpenSSH key

bEncrypt = True
unencryptedKeyStr = key.toOpenSshPrivateKey(bEncrypt)
success = key.SaveText(unencryptedKeyStr,"unencrypted_openssh.pem")
if (success != True):
    print(key.lastErrorText())
    sys.exit()

#  Save to an encrypted OpenSSH PEM file:

bEncrypt = False
#key.put_Password("myPassword")
encryptedKeyStr = key.toOpenSshPrivateKey(bEncrypt)
success = key.SaveText(encryptedKeyStr,"encrypted_openssh.pem")
if (success != True):
    print(key.lastErrorText())
    sys.exit()

print("Done!")
