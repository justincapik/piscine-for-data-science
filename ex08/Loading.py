def ft_tqdm(lst: range) -> None:

    width = 87

    for l in range(len(lst)):
        l += 1
        percentage = int(l/len(lst) * 100)

        whitecount = int(width * percentage / 100)

        progressbar = "█" * min(whitecount, width) + " " * (width - whitecount)

        print ("{:3d}%|".format(percentage) + progressbar + "| {:d}/{:d}".format(l, len(lst)), end="\r")
        
        yield