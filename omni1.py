#!/usr/bin/env python3
import random
import time
import os

class Culture:
    def __init__(self, name, numbers, letters, lore):
        self.name = name
        self.numbers = numbers  # dict: symbol -> value
        self.letters = letters  # dict: symbol -> value
        self.lore = lore
        self.seen_symbols = set()
        self.mastered_symbols = set()
        self.seen_letters = set()
        self.mastered_letters = set()

    def reveal_next_symbol(self):
        for symbol in self.numbers:
            if symbol not in self.seen_symbols:
                self.seen_symbols.add(symbol)
                return symbol, self.numbers[symbol]
        return None, None

    def reveal_next_letter(self):
        for letter in self.letters:
            if letter not in self.seen_letters:
                self.seen_letters.add(letter)
                return letter, self.letters[letter]
        return None, None

    def mark_mastered(self, symbol):
        self.mastered_symbols.add(symbol)

    def mark_mastered_letter(self, letter):
        self.mastered_letters.add(letter)

    def all_numbers_mastered(self):
        return set(self.numbers.keys()) == self.mastered_symbols

    def all_letters_mastered(self):
        return set(self.letters.keys()) == self.mastered_letters

    def display_grid(self):
        grid = []
        for symbol in self.numbers:
            if symbol in self.mastered_symbols:
                grid.append(f"[{symbol}]")
            elif symbol in self.seen_symbols:
                grid.append(f"({symbol})")
            else:
                grid.append("[ ]")
        print("Number Mastery Grid:")
        print(" ".join(grid))

        if self.seen_letters:
            grid = []
            for letter in self.letters:
                if letter in self.mastered_letters:
                    grid.append(f"[{letter}]")
                elif letter in self.seen_letters:
                    grid.append(f"({letter})")
                else:
                    grid.append("[ ]")
            print("Letter Mastery Grid:")
            print(" ".join(grid))

class OMNIGame:
    def __init__(self):
        self.cultures = [
            Culture(
                "Pythagorean",
                {"α": 1, "β": 2, "γ": 3, "δ": 4, "ε": 5, "ζ": 6, "η": 7, "θ": 8, "ι": 9, "κ": 10},
                {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "K": 10},
                "Number is the ruler of forms and ideas."
            ),
            Culture(
                "Hermetic",
                {"𓏺": 1, "𓏻": 2, "𓏼": 3, "𓏽": 4, "𓏾": 5, "𓏿": 6, "𓐀": 7, "𓐁": 8, "𓐂": 9, "𓎆": 10},
                {},
                "That which is below is like that which is above."
            ),
            Culture(
                "Kabbalistic",
                {"א": 1, "ב": 2, "ג": 3, "ד": 4, "ה": 5, "ו": 6, "ז": 7, "ח": 8, "ט": 9, "י": 10},
                {"א": 1, "ב": 2, "ג": 3, "ד": 4, "ה": 5, "ו": 6, "ז": 7, "ח": 8, "ט": 9, "י": 10},
                "In the beginning was the Word, and the Word was with numbers."
            ),
            Culture(
                "Vedantic",
                {"१": 1, "२": 2, "३": 3, "४": 4, "५": 5, "६": 6, "७": 7, "८": 8, "९": 9, "१०": 10},
                {},
                "Brahman is existence, consciousness, and bliss - expressed through number."
            ),
            Culture(
                "Mayan",
                {"●": 1, "●●": 2, "●●●": 3, "●●●●": 4, "▬": 5, "●▬": 6, "●●▬": 7, "●●●▬": 8, "●●●●▬": 9, "▬▬": 10},
                {},
                "Time is a circle, and in circles, all numbers return to their source."
            ),
            Culture(
                "Sumerian",
                {"𒐕": 1, "𒐖": 2, "𒐗": 3, "𒐘": 4, "𒐙": 5, "𒐚": 6, "𒐛": 7, "𒐜": 8, "𒐝": 9, "𒐞": 10},
                {},
                "The first civilization to write numbers in clay."
            ),
            Culture(
                "Babylonian",
                {"𒁹": 1, "𒌋": 10, "𒐕": 2, "𒐖": 3, "𒐗": 4, "𒐘": 5, "𒐙": 6, "𒐚": 7, "𒐛": 8, "𒐜": 9},
                {},
                "Babylonian mathematics: base-60, cuneiform, and the roots of algebra."
            ),
        ]
        self.player_stats = {
            "consciousness_level": 1,
            "math_skill_multiplier": 1.0,
            "mastered_cultures": [],
            "incarnation_count": 0,
            "total_formulas_solved": 0
        }
        self.current_culture = None
        self.current_session_score = 0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_matrix_intro(self):
        print("=" * 60)
        print("🌌 O M N I - The Matrix of Ancient Wisdom 🌌")
        print("=" * 60)
        print("Reality is but patterns of number and symbol...")
        print("Each incarnation reveals deeper truths...")
        print("Break through the dimensions of mathematical consciousness...")
        print("=" * 60)
        time.sleep(2)

    def incarnate(self):
        self.player_stats["incarnation_count"] += 1
        self.current_culture = random.choice(self.cultures)
        self.current_session_score = 0

        self.clear_screen()
        print(f"\n🔮 INCARNATION #{self.player_stats['incarnation_count']} 🔮")
        print(f"Philosophy: {self.current_culture.name}")
        print(f"Lore: {self.current_culture.lore}")
        print("-" * 50)
        self.current_culture.display_grid()
        print("-" * 50)
        input("\nPress Enter to begin your trials...")

    def generate_formula_challenge(self):
        base_difficulty = self.player_stats["consciousness_level"]
        # Use only seen symbols for challenges
        seen = list(self.current_culture.seen_symbols)
        if not seen:
            # If nothing seen, reveal the first symbol
            symbol, value = self.current_culture.reveal_next_symbol()
            return f"Memorize this new symbol: {symbol} = {value}", value, f"{symbol} = {value}", symbol, "number"
        symbol = random.choice(seen)
        value = self.current_culture.numbers[symbol]
        operation = random.choice(['+', '*', '-'])
        # Pick a second symbol
        seen2 = [s for s in seen if s != symbol]
        if seen2:
            symbol2 = random.choice(seen2)
            value2 = self.current_culture.numbers[symbol2]
        else:
            symbol2 = symbol
            value2 = value
        if operation == '+':
            answer = value + value2
            question = f"What is {symbol} + {symbol2}?"
        elif operation == '*':
            answer = value * value2
            question = f"What is {symbol} × {symbol2}?"
        else:
            if value >= value2:
                answer = value - value2
                question = f"What is {symbol} - {symbol2}?"
            else:
                answer = value2 - value
                question = f"What is {symbol2} - {symbol}?"
        return question, answer, f"({value} {operation} {value2} = {answer})", symbol, "number"

    def solve_formulas(self):
        formulas_in_session = 0
        consecutive_correct = 0
        while formulas_in_session < 5:
            self.clear_screen()
            print(f"🧮 Formula Challenge #{formulas_in_session + 1}/5")
            print(f"Consciousness Level: {self.player_stats['consciousness_level']}")
            print(f"Math Skill Multiplier: {self.player_stats['math_skill_multiplier']:.1f}x")
            print(f"Session Score: {self.current_session_score}")
            print("-" * 40)
            self.current_culture.display_grid()
            print("-" * 40)
            # Reveal a new symbol if not all seen
            if not self.current_culture.all_numbers_mastered():
                symbol, value = self.current_culture.reveal_next_symbol()
                if symbol:
                    print(f"🆕 New symbol unlocked: {symbol} = {value}")
                    print("Memorize this symbol to master the culture!")
            question, correct_answer, explanation, symbol, typ = self.generate_formula_challenge()
            print(f"\n{question}")
            try:
                start_time = time.time()
                user_answer = int(input("Your answer: "))
                solve_time = time.time() - start_time
                if user_answer == correct_answer:
                    consecutive_correct += 1
                    time_bonus = max(0, 10 - int(solve_time))
                    base_points = 10 * self.player_stats['consciousness_level']
                    total_points = int(base_points * self.player_stats['math_skill_multiplier']) + time_bonus
                    self.current_session_score += total_points
                    print(f"✨ CORRECT! {explanation}")
                    print(f"Points earned: {total_points} (Base: {base_points}, Multiplier: {self.player_stats['math_skill_multiplier']:.1f}x, Time bonus: {time_bonus})")
                    if typ == "number":
                        self.current_culture.mark_mastered(symbol)
                    if consecutive_correct >= 3:
                        print("🌟 BREAKTHROUGH! Your consciousness expands!")
                        self.level_up()
                        consecutive_correct = 0
                else:
                    consecutive_correct = 0
                    print(f"❌ Incorrect. The answer was {correct_answer}. {explanation}")
                    print("The matrix tightens its grip... but wisdom comes through practice.")
            except ValueError:
                consecutive_correct = 0
                print("❌ Invalid input. The cosmic forces require numerical answers.")
            formulas_in_session += 1
            self.player_stats["total_formulas_solved"] += 1
            if formulas_in_session < 5:
                input("\nPress Enter for next challenge...")

    def level_up(self):
        self.player_stats["consciousness_level"] += 1
        self.player_stats["math_skill_multiplier"] += 0.16
        print(f"🚀 CONSCIOUSNESS LEVEL UP! Now at level {self.player_stats['consciousness_level']}")
        print(f"🧠 Math skill multiplier increased to {self.player_stats['math_skill_multiplier']:.2f}x")
        if self.player_stats["math_skill_multiplier"] >= 6.16:
            print("🌌 You have achieved the 616% TRANSCENDENCE! The matrix bends to your will!")

    def end_incarnation(self):
        self.clear_screen()
        print("🔮 INCARNATION COMPLETE 🔮")
        print("-" * 40)
        print(f"Philosophy mastered: {self.current_culture.name}")
        print(f"Session Score: {self.current_session_score}")
        print(f"Total Incarnations: {self.player_stats['incarnation_count']}")
        print(f"Consciousness Level: {self.player_stats['consciousness_level']}")
        print(f"Math Skill Multiplier: {self.player_stats['math_skill_multiplier']:.2f}x")
        print(f"Total Formulas Solved: {self.player_stats['total_formulas_solved']}")
        print("-" * 40)
        if self.current_session_score > 100:
            culture = self.current_culture.name
            if culture not in self.player_stats["mastered_cultures"]:
                self.player_stats["mastered_cultures"].append(culture)
                print(f"🏆 CULTURE MASTERED: {culture}")
        print(f"Mastered Cultures: {', '.join(self.player_stats['mastered_cultures']) if self.player_stats['mastered_cultures'] else 'None yet'}")

    def play(self):
        self.display_matrix_intro()
        while True:
            choice = input("\n[P]lay new incarnation, [S]tats, or [Q]uit: ").lower()
            if choice == 'p':
                self.incarnate()
                self.solve_formulas()
                self.end_incarnation()
            elif choice == 's':
                self.clear_screen()
                print("📊 OMNI STATISTICS 📊")
                print("-" * 30)
                for key, value in self.player_stats.items():
                    print(f"{key.replace('_', ' ').title()}: {value}")
                print("-" * 30)
            elif choice == 'q':
                print("\n🌌 Until next incarnation, seeker of truth... 🌌")
                break
            else:
                print("Invalid choice. The matrix requires clear intention.")

if __name__ == "__main__":
    game = OMNIGame()
    game.play()