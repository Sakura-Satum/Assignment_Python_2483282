import break_abbrevs


def remove_duplicates(abr_dict):
    ''' brake abbreviation  and return abbreviation dictionary - {tree_name [(Abbreviation,value)]} '''
    trees = list(abr_dict)
    tree_length = len(trees)

    for i in range(tree_length):
        checking_tree = abr_dict[trees[i]][:]
        for abr in checking_tree:
            duplicate = False
            # check whether abbreviations are duplicate within different tree names and remove
            for a in range(i+1, tree_length):
                next_check_list = abr_dict[trees[a]][:]
                for check in next_check_list:
                    if abr[0] == check[0]:
                        duplicate = True
                        abr_dict[trees[a]].remove(check)
                        print(abr_dict[trees[a]])
            # check whether duplicated abbreviations are duplicate in the tree name and remove
            if duplicate:
                remove_val = abr[0]
                for curent_abr in checking_tree:
                    if remove_val == curent_abr[0]:
                        abr_dict[trees[i]].remove(curent_abr)
                print(abr_dict)

    return abr_dict


def find_lowest_abri():
    ''' Print tree name and lowest valued abbreviation to satum_tree_abbrevs.txt '''

    final_abr_list = []
    trees = list(trees_list)
    for tree in trees:
        if len(tree_dict[tree]) == 0:
            final_abr_list.append(tree)
            final_abr_list.append(' - ')
        else:
            lowest_val = tree_dict[tree][0][1]
            lowest_abri = tree_dict[tree][0][0]
            lowest_abri_list = ''
            for i in range(len(tree_dict[tree])):
                if lowest_val > tree_dict[tree][i][1]:
                    lowest_val = tree_dict[tree][i][1]
                    lowest_abri = tree_dict[tree][i][0]
            for i in range(len(tree_dict[tree])):
                if lowest_val == tree_dict[tree][i][1]:
                    lowest_abri_list = lowest_abri_list + ' ' +tree_dict[tree][i][0]
            final_abr_list.append(tree)
            final_abr_list.append(lowest_abri_list)
    # write final abbreviations to the .txt file
    with open("satum_trees_abbrevs.txt", mode='w') as file:
        file.write('')
        with open("satum_trees_abbrevs.txt", mode='a') as file:
            for abr in final_abr_list:
                file.write(abr + '\n')


# get valued abbreviation list
trees_list = break_abbrevs.assign_values()
tree_dict = break_abbrevs.make_abbry(trees_list)
# remove duplicates
duplicate_removed_tree = remove_duplicates(tree_dict)
print(tree_dict)
# find lowest value
find_lowest_abri()




