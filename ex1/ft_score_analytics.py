
import sys


def list_score(argc: int) -> list[int]:
    score = []
    i = 1
    while i < argc:
        try:
            score.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1
    return score


def score_analytics() -> None:
    score = list_score(len(sys.argv))
    if len(score) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        print(f"Scores processed: {score}")
        print(f"Total players: {len(score)}")
        print(f"Total score: {sum(score)}")
        print(f"Average score: {round((sum(score)/len(score)), 2)}")
        print(f"High score: {max(score)}")
        print(f"Low score: {min(score)}")
        print(f"Score range: {(max(score)-(min(score)))}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_analytics()
