from totalsegmentator.python_api import totalsegmentator

def main():
    input_path='/home/abigail/mphys/CT_WHOLE_CNS.nii'
    output_path= '/home/abigail/mphys/ethan_test_output'

    print('zoom')
    totalsegmentator(input_path,output_path,task = 'craniofacial_structures')
    print('\nDone!')

if __name__ == "__main__":
 main()
