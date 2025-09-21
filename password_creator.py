#!/usr/bin/env python3
"""
Password Creator - Secure Password Generator
A comprehensive tool for generating strong, customizable passwords
"""

import random
import string
import secrets
import argparse
import json
from typing import List, Dict, Any


class PasswordCreator:
    """A secure password generator with customizable options"""
    
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.ambiguous_chars = "0O1lI"  # Characters that might be confusing
        
    def generate_password(self, 
                         length: int = 12,
                         use_uppercase: bool = True,
                         use_lowercase: bool = True,
                         use_digits: bool = True,
                         use_special: bool = True,
                         exclude_ambiguous: bool = False,
                         custom_chars: str = "",
                         min_uppercase: int = 1,
                         min_lowercase: int = 1,
                         min_digits: int = 1,
                         min_special: int = 1) -> str:
        """
        Generate a secure password with specified criteria
        
        Args:
            length: Password length (minimum 4)
            use_uppercase: Include uppercase letters
            use_lowercase: Include lowercase letters
            use_digits: Include digits
            use_special: Include special characters
            exclude_ambiguous: Exclude ambiguous characters (0, O, 1, l, I)
            custom_chars: Additional custom characters to include
            min_uppercase: Minimum number of uppercase letters
            min_lowercase: Minimum number of lowercase letters
            min_digits: Minimum number of digits
            min_special: Minimum number of special characters
            
        Returns:
            Generated password string
        """
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")
            
        # Build character pool
        char_pool = ""
        required_chars = []
        
        if use_lowercase:
            chars = self.lowercase
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous_chars)
            char_pool += chars
            required_chars.extend(secrets.choice(chars) for _ in range(min_lowercase))
            
        if use_uppercase:
            chars = self.uppercase
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous_chars)
            char_pool += chars
            required_chars.extend(secrets.choice(chars) for _ in range(min_uppercase))
            
        if use_digits:
            chars = self.digits
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous_chars)
            char_pool += chars
            required_chars.extend(secrets.choice(chars) for _ in range(min_digits))
            
        if use_special:
            char_pool += self.special_chars
            required_chars.extend(secrets.choice(self.special_chars) for _ in range(min_special))
            
        if custom_chars:
            char_pool += custom_chars
            
        if not char_pool:
            raise ValueError("At least one character type must be enabled")
            
        if len(required_chars) > length:
            raise ValueError("Minimum requirements exceed password length")
            
        # Generate remaining characters
        remaining_length = length - len(required_chars)
        additional_chars = [secrets.choice(char_pool) for _ in range(remaining_length)]
        
        # Combine and shuffle all characters
        all_chars = required_chars + additional_chars
        secrets.SystemRandom().shuffle(all_chars)
        
        return ''.join(all_chars)
    
    def generate_passphrase(self, 
                           word_count: int = 4,
                           separator: str = "-",
                           capitalize: bool = True,
                           add_numbers: bool = False) -> str:
        """
        Generate a memorable passphrase using common words
        
        Args:
            word_count: Number of words in the passphrase
            separator: Character to separate words
            capitalize: Capitalize first letter of each word
            add_numbers: Add random numbers to the passphrase
            
        Returns:
            Generated passphrase string
        """
        # Common words for passphrases (you can expand this list)
        words = [
            "apple", "brave", "cloud", "dream", "eagle", "flame", "grace", "happy",
            "magic", "ocean", "piano", "quiet", "river", "smile", "tiger", "unity",
            "village", "wonder", "yellow", "zebra", "anchor", "bright", "castle",
            "dolphin", "forest", "guitar", "honey", "island", "jungle", "knight",
            "lemon", "mountain", "nature", "orange", "purple", "rescue", "sunset",
            "travel", "unique", "victory", "wisdom", "galaxy", "thunder", "rainbow"
        ]
        
        selected_words = [secrets.choice(words) for _ in range(word_count)]
        
        if capitalize:
            selected_words = [word.capitalize() for word in selected_words]
            
        passphrase = separator.join(selected_words)
        
        if add_numbers:
            numbers = ''.join(str(secrets.randbelow(10)) for _ in range(2))
            passphrase += separator + numbers
            
        return passphrase
    
    def check_password_strength(self, password: str) -> Dict[str, Any]:
        """
        Analyze password strength and provide feedback
        
        Args:
            password: Password to analyze
            
        Returns:
            Dictionary with strength analysis
        """
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        else:
            feedback.append("Password should be at least 8 characters long")
            
        # Character variety checks
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in self.special_chars for c in password)
        
        variety_count = sum([has_lower, has_upper, has_digit, has_special])
        score += variety_count
        
        if not has_lower:
            feedback.append("Add lowercase letters")
        if not has_upper:
            feedback.append("Add uppercase letters")
        if not has_digit:
            feedback.append("Add numbers")
        if not has_special:
            feedback.append("Add special characters")
            
        # Determine strength level
        if score >= 6:
            strength = "Very Strong"
        elif score >= 4:
            strength = "Strong"
        elif score >= 2:
            strength = "Medium"
        else:
            strength = "Weak"
            
        return {
            "score": score,
            "max_score": 6,
            "strength": strength,
            "feedback": feedback,
            "has_lowercase": has_lower,
            "has_uppercase": has_upper,
            "has_digits": has_digit,
            "has_special": has_special,
            "length": len(password)
        }
    
    def generate_multiple_passwords(self, count: int = 5, **kwargs) -> List[str]:
        """Generate multiple passwords with the same criteria"""
        return [self.generate_password(**kwargs) for _ in range(count)]


def main():
    """Command line interface for the password creator"""
    parser = argparse.ArgumentParser(description="Secure Password Generator")
    
    # Password generation options
    parser.add_argument("-l", "--length", type=int, default=12, 
                       help="Password length (default: 12)")
    parser.add_argument("-c", "--count", type=int, default=1,
                       help="Number of passwords to generate (default: 1)")
    parser.add_argument("--no-uppercase", action="store_true",
                       help="Exclude uppercase letters")
    parser.add_argument("--no-lowercase", action="store_true",
                       help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true",
                       help="Exclude digits")
    parser.add_argument("--no-special", action="store_true",
                       help="Exclude special characters")
    parser.add_argument("--exclude-ambiguous", action="store_true",
                       help="Exclude ambiguous characters (0, O, 1, l, I)")
    parser.add_argument("--custom-chars", type=str, default="",
                       help="Additional custom characters to include")
    
    # Passphrase options
    parser.add_argument("-p", "--passphrase", action="store_true",
                       help="Generate passphrase instead of password")
    parser.add_argument("-w", "--words", type=int, default=4,
                       help="Number of words in passphrase (default: 4)")
    parser.add_argument("-s", "--separator", type=str, default="-",
                       help="Separator for passphrase words (default: -)")
    
    # Analysis options
    parser.add_argument("--analyze", type=str,
                       help="Analyze strength of provided password")
    
    args = parser.parse_args()
    
    creator = PasswordCreator()
    
    # Password analysis mode
    if args.analyze:
        analysis = creator.check_password_strength(args.analyze)
        print(f"\n🔍 Password Analysis for: {args.analyze}")
        print("=" * 50)
        print(f"Strength: {analysis['strength']} ({analysis['score']}/{analysis['max_score']})")
        print(f"Length: {analysis['length']} characters")
        print(f"Has lowercase: {'✓' if analysis['has_lowercase'] else '✗'}")
        print(f"Has uppercase: {'✓' if analysis['has_uppercase'] else '✗'}")
        print(f"Has digits: {'✓' if analysis['has_digits'] else '✗'}")
        print(f"Has special chars: {'✓' if analysis['has_special'] else '✗'}")
        
        if analysis['feedback']:
            print("\n💡 Suggestions for improvement:")
            for suggestion in analysis['feedback']:
                print(f"  • {suggestion}")
        return
    
    print("\n🔐 Password Creator")
    print("=" * 30)
    
    # Passphrase generation mode
    if args.passphrase:
        print(f"Generating {args.count} passphrase(s):\n")
        for i in range(args.count):
            passphrase = creator.generate_passphrase(
                word_count=args.words,
                separator=args.separator,
                add_numbers=True
            )
            print(f"{i+1}. {passphrase}")
            
            # Show strength analysis for first passphrase
            if i == 0:
                analysis = creator.check_password_strength(passphrase)
                print(f"   Strength: {analysis['strength']} ({analysis['length']} characters)")
    
    # Password generation mode
    else:
        options = {
            'length': args.length,
            'use_uppercase': not args.no_uppercase,
            'use_lowercase': not args.no_lowercase,
            'use_digits': not args.no_digits,
            'use_special': not args.no_special,
            'exclude_ambiguous': args.exclude_ambiguous,
            'custom_chars': args.custom_chars
        }
        
        print(f"Generating {args.count} password(s) with {args.length} characters:\n")
        
        for i in range(args.count):
            password = creator.generate_password(**options)
            print(f"{i+1}. {password}")
            
            # Show strength analysis for first password
            if i == 0:
                analysis = creator.check_password_strength(password)
                print(f"   Strength: {analysis['strength']} ({analysis['score']}/{analysis['max_score']})")
    
    print("\n💡 Tips:")
    print("  • Use unique passwords for each account")
    print("  • Consider using a password manager")
    print("  • Enable two-factor authentication when possible")


if __name__ == "__main__":
    main()
