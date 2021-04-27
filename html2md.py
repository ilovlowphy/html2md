import os
import pypandoc

def main():
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            input_file = os.path.join(root, name)
            file_name, ext = os.path.splitext(input_file)
            if ext==".html":
                output_file = file_name+".md"
                pypandoc.convert(input_file, 'md', format='html',outputfile=output_file)
        # for name in dirs:
        #     print(os.path.join(root, name))

if __name__=="__main__" :
    main()