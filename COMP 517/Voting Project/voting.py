def dictatorship(preferences, agent):
    """
    Dictatorship Voting Method -
    The winner is the candidate ranked highest by a single chosen agent.

    Args:
        preferences: An object to get information about candidates and voters.
        agent: The chosen dictator agent.

    Returns:
        The candidate ranked first by the dictator.
    """
    if agent not in preferences.voters():
        raise ValueError("Invalid agent")

    candidates = preferences.candidates()

    for candidate in candidates:
        if preferences.get_preference(candidate, agent) == 0:
            return candidate

    raise RuntimeError("No valid candidate found. Check preferences data.")


def scoring_rule(preferences, score_vector, tie_break_agent):
    """
    Scoring Rule Voting Method -
    Each rank is assigned a score, and the candidate with the highest total wins.

    Args:
        preferences: An object to access candidates, voters, and preferences.
        score_vector: A list of scores for each rank.
        tie_break_agent: A voter to decide the winner in case of a tie.

    Returns:
        The candidate with the highest total score.
    """
    candidates = preferences.candidates()
    voters = preferences.voters()

    if not score_vector or len(score_vector) != len(candidates):
        raise ValueError("Score vector must match the number of candidates")

    scores = {candidate: 0 for candidate in candidates}

    for voter in voters:
        for candidate in candidates:
            rank = preferences.get_preference(candidate, voter)
            if rank is not None:
                scores[candidate] += score_vector[rank]

    max_score = max(scores.values())
    possible_winners = [
        candidate for candidate, score in scores.items() if score == max_score
    ]

    return _tie_break(preferences, possible_winners, tie_break_agent)


def plurality(preferences, tie_break):
    """
    Plurality Voting Method -
    The winner is the candidate with the most first-place votes.

    Args:
        preferences: Preference object to get candidates and voter rankings.
        tie_break: Agent used for tie-breaking in case of a tie.

    Returns:
        The candidate with the most first-place votes.
    """
    candidates = preferences.candidates()
    first_place_counts = {candidate: 0 for candidate in candidates}

    for voter in preferences.voters():
        for candidate in candidates:
            if preferences.get_preference(candidate, voter) == 0:
                first_place_counts[candidate] += 1
                break

    max_count = max(first_place_counts.values())
    possible_winners = [
        candidate
        for candidate, count in first_place_counts.items()
        if count == max_count
    ]

    return _tie_break(preferences, possible_winners, tie_break)


def veto(preferences, tie_break):
    """
    Veto Voting Method -
    Each voter can "veto" their least preferred candidate, reducing their score.

    Args:
        preferences: Preference object for accessing rankings.
        tie_break: Agent used for tie-breaking.

    Returns:
        The candidate with the highest score after vetoing.
    """
    candidates = preferences.candidates()
    scores = {candidate: 0 for candidate in candidates}
    num_candidates = len(candidates)

    for voter in preferences.voters():
        last_place = None
        for candidate in candidates:
            if preferences.get_preference(candidate, voter) == num_candidates - 1:
                last_place = candidate
                break

        for candidate in candidates:
            if candidate != last_place:
                scores[candidate] += 1

    max_score = max(scores.values())
    possible_winners = [
        candidate for candidate, score in scores.items() if score == max_score
    ]

    return _tie_break(preferences, possible_winners, tie_break)


def borda(preferences, tie_break):
    """
    Borda Voting Method -
    Candidates receive points based on their ranking by each voter.

    Args:
        preferences: Preference object for accessing rankings.
        tie_break: Agent used for tie-breaking.

    Returns:
        The candidate with the highest Borda score.
    """
    candidates = preferences.candidates()
    num_candidates = len(candidates)
    scores = {candidate: 0 for candidate in candidates}

    for voter in preferences.voters():
        for candidate in candidates:
            rank = preferences.get_preference(candidate, voter)
            if rank is not None:
                scores[candidate] += num_candidates - 1 - rank

    max_score = max(scores.values())
    possible_winners = [
        candidate for candidate, score in scores.items() if score == max_score
    ]

    return _tie_break(preferences, possible_winners, tie_break)


def STV(preferences, tie_break):
    """
    Single Transferable Vote (STV) Method -
    Eliminate the candidate with the fewest first-place votes each round.

    Args:
        preferences: Preference object for accessing rankings.
        tie_break: Agent used for tie-breaking.

    Returns:
        The last remaining candidate.
    """
    candidates = preferences.candidates().copy()

    while len(candidates) > 1:
        first_place_counts = {candidate: 0 for candidate in candidates}

        for voter in preferences.voters():
            for candidate in candidates:
                if preferences.get_preference(candidate, voter) == 0:
                    first_place_counts[candidate] += 1
                    break

        min_count = min(first_place_counts.values())
        eliminated = [
            candidate
            for candidate in candidates
            if first_place_counts[candidate] == min_count
        ]

        if len(eliminated) == len(candidates):  # Tie case
            return _tie_break(preferences, candidates, tie_break)

        candidates = [
            candidate for candidate in candidates if candidate not in eliminated
        ]

    return candidates[0]


def _tie_break(preferences, possible_winners, tie_break_agent):
    """
    Tie-breaking Method -
    Selects the winner based on the preference of a specific agent.

    Args:
        preferences: Preference object for accessing voter rankings.
        possible_winners: List of tied candidates.
        tie_break_agent: The agent used for tie-breaking.

    Returns:
        The candidate ranked highest by the tie-break agent.
    """
    if not possible_winners:
        return None
    if tie_break_agent not in preferences.voters():
        raise ValueError("Invalid tie-break agent")

    return min(
        possible_winners, key=lambda x: preferences.get_preference(x, tie_break_agent)
    )
