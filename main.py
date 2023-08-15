from project_distribution import gender_nums, race_nums, utils

def main():

    df = utils.read_file("gender_race.csv")
    print(gender_nums.gen_gender_output(df))
    print(race_nums.gen_race_output(df))

if __name__== "__main__" :
    main()  
    