# prompt for the applicant's name, GPA and disciplinary cases, and print the output
def main():
    name = input("What is your name: ").strip()
    formatted_name = format_applicant(name)
    try:
        gpa = float(input("What is your GPA: "))
        cases = int(input("How many disciplinary cases do you have: "))
        eligibility = get_eligibility(gpa, cases)
        if eligibility is not None:
            message = get_message(eligibility)
            print(
                f"{formatted_name} has a GPA of {gpa:.2f} with {cases} disciplinary case(s) — {eligibility}. {message}"
            )
        else:
            return None
    except ValueError:
        pass


# return the applicant's name in title case
def format_applicant(n):
    n = n.title()
    return n


# return the eligibility of the applicant based on their gpa and disciplinary cases
def get_eligibility(gpa, cases):
    if gpa < 0 or gpa > 4.0 or cases < 0:
        return None
    elif cases > 0:
        return "Ineligible"
    elif gpa >= 3.7:
        return "Full Scholarship"
    elif gpa >= 3.0:
        return "Partial Scholarship"
    else:
        return "Not Qualified"


# return a message based on the eligibility category of the applicant
def get_message(eligibility):
    match eligibility:
        case "Full Scholarship":
            return "Fully funded!"
        case "Partial Scholarship":
            return "Half funded."
        case "Not Qualified":
            return "Keep working hard."
        case "Ineligible":
            return "Disciplinary record disqualifies you."


if __name__ == "__main__":
    main()
