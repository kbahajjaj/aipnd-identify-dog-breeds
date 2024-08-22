#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Khalid Salim
# DATE CREATED: April 1st, 2024                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir, system

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    ###------Retrieve the filenames from folder pet_images/------###
    filename_list = listdir(image_dir)
    
    # Check: Print 10 of the filenames from folder pet_images/
    #print("\nPrints 10 filenames from folder pet_images/")
    #for idx in range(0, 10, 1):
    #    print("{:2d} file: {:>26}".format(idx + 1, filename_list[idx]))
    
    ###------Building the filename/image-label key/value dictionary------### 

    # Creates empty dictionary named results_dic
    results_dic = dict()

    # Determines number of items in dictionary
    #items_in_dic = len(results_dic)
    #print("\nEmpty Dictionary results_dic - n items=", items_in_dic)
    
    # Creating pet_labels list from filename_list
    filename_alphanum = [filename.lower().split("_") for filename in filename_list]
    pet_labels = [[' '.join(filename[:-1]).strip()] for filename in filename_alphanum]
    
    # Check: printing the pet labels
    #print(pet_labels)

    # Using dictionary comprehensions, Adds new key-value pairs to dictionary ONLY when key doesn't 
    # already exist. This dictionary's value is a List that contains only one item - the pet image label  
    results_dic = { key:value for (key,value) in zip(filename_list, pet_labels)\
                   if key not in results_dic.keys()}
    
    # Check: Printing results_dic & its length
    #print(results_dic)
    #print(len(results_dic))

    # Check: Printing results_dic keys (filenames) versus values (pet_labels) in a listed manner
    #for i in range(10):
    #    print("key: {}, value: {}".format(filename_list[i], results_dic[filename_list[i]]), '\n')
    
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    return results_dic