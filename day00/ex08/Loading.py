def ft_tqdm(lst: range) -> None:

    width = 87

    for it in range(len(lst)):
        it += 1
        percentage = int(it/len(lst) * 100)

        whitecount = int(width * percentage / 100)

        progressbar = "█" * min(whitecount, width) + " " * (width - whitecount)

        print("{:3d}%|".format(percentage) +
              progressbar + "| {:d}/{:d}".format(it, len(lst)), end="\r")

        yield
