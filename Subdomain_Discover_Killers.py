'''
A basic script to Discover Subdomains implemented with threading
KILLER007
'''
import requests, optparse
import threading

def num_of_lines():
    num_lines=0
    with open(wordlist,"r") as fp:
        for line in fp:
            num_lines +=1           
        return num_lines

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="[-]Enter Target URL in format: Google.com")
    options = parser.parse_args()[0]
    if not options.target:
        parser.error("[-] Please Specify the target URL, Use --help for Help")
    else:
        return options


def request(url):
    try:
        response = requests.get("http://" + url)         
        return response
    except requests.exceptions.ConnectionError:          
        pass


def subdomain(starto,endo,url):
    start_line = starto                 
    end_line = endo 
    with open(wordlist, "r") as wordlist_file: 
        for line in range(start_line):         
            wordlist_file.readline()
        for line in wordlist_file:
            word = line.strip()                       
            test_url = word + "." + url               
#            print("[+]Trying --> "+test_url)
            response = request(test_url)              
            if response:                              
               print ("\n[--------------------------------------------------]\nSubdomain Discoverd --> " + test_url +"\n[--------------------------------------------------]\n")

            start_line +=1
            if(start_line==end_line):      
                break

options = get_args()
print("---------------------------------------\n\t\tKiller007\n---------------------------------------")
try:
    wordlist="subdomain_wordlist_top5000.txt"
    no_of_threads = 5           
    total_words = num_of_lines()               
    each_thread_words = int(total_words/no_of_threads) 

    begin=0                                             
    end=each_thread_words       
    for i in range(no_of_threads):                      
        t1 = threading.Thread(target=subdomain, args=(begin,end,options.target)) 
        t1.start()
        begin += each_thread_words
        end += each_thread_words
      
except KeyboardInterrupt:               
    print ("\nExiting.....")

