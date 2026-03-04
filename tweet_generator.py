import random

def generate_tweets(brand, industry, campaign, product, style):

    openings = [
        "Ready to experience something new?",
        "The future starts today.",
        "Big innovation is here.",
        "Something exciting is coming.",
        "Level up your lifestyle.",
        "Introducing a new era.",
        "Your journey starts now.",
        "Get ready for the next big thing."
    ]

    benefits = [
        f"designed to transform the {industry} experience",
        "built for modern lifestyles",
        "crafted for people who demand the best",
        "created with innovation at its core",
        "built for performance and reliability",
        "engineered to deliver excellence",
        "designed to inspire confidence",
        "made to simplify your life"
    ]

    calls = [
        "Try it today!",
        "Discover more now.",
        "Join the movement.",
        "Upgrade today.",
        "Experience it now.",
        "Don't miss out.",
        "See the difference.",
        "Be part of the future."
    ]

    hashtags_pool = [
        "#Innovation",
        "#NextLevel",
        "#FutureReady",
        "#Trending",
        "#SmartLiving",
        "#BrandPower",
        "#DigitalFuture",
        "#GameChanger",
        "#NewLaunch",
        "#TechLife"
    ]

    tweets = []

    for i in range(10):

        opening = random.choice(openings)
        benefit = random.choice(benefits)
        call = random.choice(calls)

        hashtags = " ".join(random.sample(hashtags_pool, 2))

        tweet = f"{opening} {brand} brings you a product {benefit}. {product}. {call} {hashtags}"

        # Twitter limit check
        tweet = tweet[:280]

        tweets.append(tweet)

    return tweets