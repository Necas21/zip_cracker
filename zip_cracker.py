import zipfile
import argparse
import sys


def check_pass(zip_file, passwd):

	try:
		print("Trying password: {}".format(passwd))
		zip_file.extractall(path="results", pwd=bytes(passwd, "utf-8"))
		print("[+] Found password: {}".format(passwd))
		print("[+] Extracting files to results...")
		return True

	except:
		pass


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-f", dest="file", help="Specify the name of a Zip file.")
	parser.add_argument("-d", dest="dictionary", help="Specify a dictionary file.")

	if len(sys.argv) == 1:
		parser.print_help(sys.stderr)
		sys.exit(1)

	args = parser.parse_args()

	print("Zip File: {}".format(args.file))
	print("Dictionary: {}".format(args.dictionary))

	zip = zipfile.ZipFile(args.file)
	dict = open(args.dictionary, "r")

	for password in dict.readlines():

		p = password.strip("\n")
		if check_pass(zip, p):
			break

	print("[*] Completed!")



if __name__ == '__main__':
	main()
