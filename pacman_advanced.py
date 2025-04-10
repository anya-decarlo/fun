def can_advance_level(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Determine if Pac-Man can advance to the next level based on various conditions.

    :param has_eaten_all_dots: bool - has the player eaten all dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can the player advance to the next level?
    """
    # Implementation based on user's specified logic
    if has_eaten_all_dots is True and power_pellet_active is True and touching_ghost is True: 
        return True 
    if has_eaten_all_dots is True and power_pellet_active is True and touching_ghost is False: 
        return True 
    if has_eaten_all_dots is True and power_pellet_active is False and touching_ghost is True: 
        return False
    if has_eaten_all_dots is True and power_pellet_active is False and touching_ghost is False: 
        return True 
    if has_eaten_all_dots is False:
        return False
    
    # This logic can be simplified to:
    # return has_eaten_all_dots and (power_pellet_active or not touching_ghost)

# Test the function with different combinations of inputs
if __name__ == "__main__":
    # Test all possible combinations
    test_cases = [
        (True, True, True),   # has_eaten_all_dots, power_pellet_active, touching_ghost
        (True, True, False),
        (True, False, True),
        (True, False, False),
        (False, True, True),
        (False, True, False),
        (False, False, True),
        (False, False, False)
    ]
    
    for case in test_cases:
        has_eaten, power_active, touching = case
        result = can_advance_level(has_eaten, power_active, touching)
        print(f"has_eaten_all_dots={has_eaten}, power_pellet_active={power_active}, touching_ghost={touching} => {result}")
