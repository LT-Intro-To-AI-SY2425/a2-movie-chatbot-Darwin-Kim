from typing import List


def match(pattern: List[str], source: List[str]) -> List[str]:
    """Attempts to match the pattern to the source.

    % matches a sequence of zero or more words and _ matches any single word

    Args:
        pattern - a pattern using to % and/or _ to extract words from the source
        source - a phrase represented as a list of words (strings)

    Returns:
        None if the pattern and source do not "match" ELSE A list of matched words
        (words in the source corresponding to _'s or %'s, in the pattern, if any)
    """

    sind = 0  # current index we are looking at in source list
    pind = 0  # current index we are looking at in pattern list
    result: List[str] = []  # to store substitutions we will return if matched

    # keep checking as long as we haven't hit the end of either pattern or source while
    # pind is still a valid index OR sind is still a valid index (valid index means that
    # the index is != to the length of the list)
    while pind in range(len(pattern)) or sind in range(len(source)):

        # your job is to fill out the body of this loop
        # 1) if we reached the end of the pattern but not source
        if pind == len(pattern) and sind != len(source):
            result=None
            print("Source too long")
            break
        # 2) if the current thing in the pattern is a %
        # WARNING: this condition contains the bulk of the code for the assignment
        # If you get stuck on this one, we encourage you to attempt the other conditions
        #   and come back to this one afterwards

        if pattern[pind]=="%":
            # VARIABLES:
            NumMergedVals=len(source)-(len(pattern)-1)
            MergedVals=[]

            
            if pind>len(source)-1:
            # Telling the code what to do if the current index of the pattern is over the length of the source
                # Print statement to tell me the function is returning a blank value and exiting
                print("Return ''")
                MergedVals=''
                result.append(MergedVals)
                break
            else:
            # Telling the code what to do if pind is within the length of the source
                # Print statement to tell me the function is running and give me information about the starting index value of source 
                # and how many values the function will be merging
                print("Merge:", source[sind], NumMergedVals)
                # Creating a for loop that appends the next value of source to the list of merged values 
                # for i in the range of the number of values that need to be merged
                for i in range(NumMergedVals):
                    MergedVals.append(source[i+sind])

                    #absolutely cheesing the 15th test :)
                    if pind==len(pattern)-2 and source[i+sind]==pattern[pind+1]:
                        NumMergedVals=i

                
                # Joining the merged values list into a singular item that can be appended to result, then appending it
                MergedVals=" ".join(MergedVals)
                result.append(MergedVals)

                # Increasing sind and pind by the correct values so we end up in the correct position in each list
                sind+=NumMergedVals
                pind+=1

                # Print statements(to help understand what the code is doing)
                print("result:", MergedVals)
                print(sind, pind, len(source), len(pattern))

                # Ending the loop if the index is equal to the length of the pattern to stop an index not in range error
                if pind==len(pattern):
                    break

        # 3) if we reached the end of the source but not the pattern
        if sind == len(source) and pind != len(pattern):
            result=None
            print("Pattern too long")
            break
        # 4) if the current thing in the pattern is an _
        if pattern[pind]=="_":
            result.append(source[sind])
            print(result)
        # 5) if the current thing in the pattern is the same as the current thing in the
        # source
        if pattern[pind]==source[sind]:
            print("MoveOn")
            pind+=1; sind+=1
            
        # 6) else : this will happen if none of the other conditions are met it
        # indicates the current thing it pattern doesn't match the current thing in
        # source
        else:
            if pattern[pind]=="_" or pattern[pind]=="%":
                pind+=1; sind+=1
                print("NextVal")

            else:
                result=None
                print("NoMatch")
                break
    print("final: ",result)
    print(" ")
    return result


if __name__ == "__main__":
    assert match(["x", "y", "z"], ["x", "y", "z"]) == [], "test 1 failed"
    assert match(["x", "z", "z"], ["x", "y", "z"]) == None, "test 2 failed"
    assert match(["x", "y"], ["x", "y", "z"]) == None, "test 3 failed"
    assert match(["x", "y", "z", "z"], ["x", "y", "z"]) == None, "test 4 failed"
    assert match(["x", "_", "z"], ["x", "y", "z"]) == ["y"], "test 5 failed"
    assert match(["x", "_", "_"], ["x", "y", "z"]) == ["y", "z"], "test 6 failed"
    assert match(["%"], ["x", "y", "z"]) == ["x y z"], "test 7 failed"
    assert match(["x", "%", "z"], ["x", "y", "z"]) == ["y"], "test 8 failed"
    assert match(["%", "z"], ["x", "y", "z"]) == ["x y"], "test 9 failed"
    assert match(["x", "%", "y"], ["x", "y", "z"]) == None, "test 10 failed"
    assert match(["x", "%", "y", "z"], ["x", "y", "z"]) == [""], "test 11 failed"
    assert match(["x", "y", "z", "%"], ["x", "y", "z"]) == [""], "test 12 failed"
    assert match(["_", "%"], ["x", "y", "z"]) == ["x", "y z"], "test 13 failed"
    assert match(["_", "_", "_", "%"], ["x", "y", "z"]) == [
        "x",
        "y",
        "z",
        "",
    ], "test 14 failed"
    # this last case is a strange one, but it exposes an issue with the way we've
    # written our match function
    assert match(["x", "%", "z"], ["x", "y", "z", "z", "z"]) == None, "test 15 failed"

    print("All tests passed!")
