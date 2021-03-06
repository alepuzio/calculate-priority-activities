# Calculate priority of the activities
--------------------------------------
This project was born after readning the comments in [this post](https://news.ycombinator.com/item?id=15686211) of HackerNews.
This application writes a file with a list of the activites and their priority (numeric index: 1 highest priority, 2 less prioritary, etc).
In detail:
* The application reads two existing files:
1. activity-date.csv (Activity,Start,End) about the duration of an activity
2. activity-importance.csv (Activity,Importance) about the importance of an activity. The meaning of importance is relative and vague. A definition can be: if you have two activites A and B in the same time, A is more important of B if doing A you can earn more money (or, lose less money) than doing B.
* The application writes one file ordered-activities.csv (Activity, Priority)


## Feature

[O] The input files can have a different order of the activities each other (now the order has to be the same, otherwise an Exception will be run)
[O] The final list can be separated in "activities already started" (start date minor than today) and "future activities" (start date major than today)
[O] The final list can be separated by the area of interest of the project (Area of responsability in GTD meaning)

## Bug

[X] Fix the unit test
[O] Resolve the TODO in the code
[O]  Organize the structure following the guidelines in [The Hitchhiker's Guide to Python!](https://docs.python-guide.org/)

## Status CI Integration
 
I use [Travis](https://travis-ci.org/)
[![Build Status](https://travis-ci.org/alepuzio/calculate-priority-activities.svg?branch=master)](https://travis-ci.org/alepuzio/calculate-priority-activities)

## Getting started

### Prerequisites

- Python 3.0+
- pip
- pytest 

### Installing

- Clone the project with *git-clone* (or download directly it)
- Have fun!

## Running the tests

- In this version the unit test are inside the module and are not completed. TDD, sorry :(

### Break down into to end to end tests

No indications

### Coding styles sheets

Please read the file [CONTRIBUTING.md](https://github.com/alepuzio/calculate-priority-activities/blob/master/CONTRIBUTING.md)

## Deployment
 
 - No package built (sorry, I'm a beginner in Python :) )
 - Run    **>>> python Main.py**
 
### Built with:

* [ViM](http://www.vim.org) - one of the best text editor I know
* [pytest](https://docs.pytest.org/en/stable/) - most famous library about the testing in Python

## Contributing

Please read the [CONTRIBUTING.md](https://github.com/alepuzio/calculate-priority-activities/blob/master/CONTRIBUTING.md) for the details about the code of conduct and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/alepuzio/calculate-priority-activities/tags). 

## Authors

* **Alessandro Puzielli** - *creator* - [Alepuzio](https://github.com/alepuzio)

See also the list of [contributors](https://github.com/alepuzio/calculate-priority-activities/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* **PurpleBooth** - to publish an [excellent template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) of README that I used in this project 
* **Yegor256** - to write the post [Elegant READMEs](https://www.yegor256.com/2019/04/23/elegant-readme.html) about the README file and the [An Open Code Base Is Not Yet an Open Source Project](https://www.yegor256.com/2018/05/08/open-source-attributes.html) for the Open Source activities
