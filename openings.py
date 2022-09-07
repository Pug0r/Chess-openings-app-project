# Remember to add the opening to the list of openings after you've finished writing the dictionary!
SCOTCH_GAME = {'name': "Scotch Game",
               'user_plays_white': '',
               'variations':
                   {'Schmidt Variation': {0: 'e2e4', 1: 'e7e5', 2: 'g1f3', 3: 'b8c6', 4: 'd2d4', 5: 'e5d4', 6: 'f3d4', 7: 'g8f6'},
                    'Classical Variation': {0: 'e2e4', 1: 'e7e5', 2: 'g1f3', 3: 'b8c6', 4: 'd2d4', 5: 'e5d4', 6: 'f3d4', 7: 'f8c5'},
                    'Scotch Gambit': {0: 'e2e4', 1: 'e7e5', 2: 'g1f3', 3: 'b8c6', 4: 'd2d4', 5: 'e5d4', 6: 'f1c4'},
                    'Goring Gambit': {0: 'e2e4', 1: 'e7e5', 2: 'g1f3', 3: 'b8c6', 4: 'd2d4', 5: 'e5d4', 6: 'c2c3'}
                    },
               }

QUEENS_GAMBIT = {'name': "Queen's Gambit",
                 'user_plays_white': '',
                 'variations':
                     {'accepted': {0: 'd2d4', 1: 'd7d5', 2: 'c2c4', 3: 'd5c4'},
                      'declined': {0: 'd2d4', 1: 'd7d5', 2: 'c2c4', 3: 'e7e6'},
                      'Slav defense': {0: 'd2d4', 1: 'd7d5', 2: 'c2c4', 3: 'c7c6'},
                      'Albin Countergambit': {0: 'd2d4', 1: 'd7d5', 2: 'c2c4', 3: 'e7e5'},
                      }
                 }

ITALIAN_GAME = {'name': "Italian Game",
                'user_plays_white': '',
                'variations':
                    {'Giuoco Piano': {0: 'e2e4', 1: 'e7e5', 2: 'g1f3', 3: 'b8c6', 4: 'f1c4', 5: 'f8c5'},
                     'Giuoco Pianissimo': {0: 'e2e4', 1: 'e7e5', 2: 'g1f3', 3: 'b8c6', 4: 'f1c4', 5: 'f8c5', 6: 'd2d3', 7: 'g8f6', 8: 'c2c3'},
                     'Evans Gambit': {0: 'e2e4', 1: 'e7e5', 2: 'g1f3', 3: 'b8c6', 4: 'f1c4', 5: 'f8c5', 6: 'b2b4'},
                     },
                }

LONDON_SYSTEM = {'name': "London System",
                 'user_plays_white': True,
                 'variations':
                     {'Mainline': {0: 'd2d4', 1: 'd7d5', 2: 'c1f4', 3: 'g8f6', 4: 'e2e3', 5: 'c7c5', 6: 'c2c3', 7: 'b8c6', 8: 'b1d2', 9: 'e7e6', 10: 'g1f3', 11: 'f8d6', 12: 'f4g3', 13: 'h7h6', 14: 'f1d3', 15: 'b7b6', 16: 'd1e2'}}
                 }

VIENNA_GAME = {'name': "Vienna Game",
               'user_plays_white': True,
               'variations':
                   {'Falkbeer Variation': {0: 'e2e4', 1: 'e7e5', 2: 'b1c3', 3: 'g8f6'},
                    'Vienna Gambit': {0: 'e2e4', 1: 'e7e5', 2: 'b1c3', 3: 'g8f6', 4: 'f2f4'}
                    }
               }

BLACKMAR_DIEMER_GAMBIT = {'name': "Blackmar-Diemer Gambit",
                          'user_plays_white': True,
                          'variations':
                              {'Mainline': {0: 'd2d4', 1: 'd7d5', 2: 'e2e4', 3: 'd5e4', 4: 'b1c3', 5: 'g8f6', 6: 'f2f3', 7: 'e4f3', 8: 'g1f3'}
                               }
                          }

SICILIAN_DEFENSE = {'name': "Sicilian Defense",
                    'user_plays_white': '',
                    'variations':
                        {'Closed Variation': {0: 'e2e4', 1: 'c7c5', 2: 'b1c3'},
                         'Open Variation': {0: 'e2e4', 1: 'c7c5', 2: 'g1f3', 3: 'd7d6', 4: 'd2d4', 5: 'c5d4', 6: 'f3d4'},
                         'Dragon Variation': {0: 'e2e4', 1: 'c7c5', 2: 'g1f3', 3: 'd7d6', 4: 'd2d4', 5: 'c5d4', 6: 'f3d4', 7: 'g8f6', 8: 'b1c3', 9: 'g7g6'}
                        }
                    }

THE_FRENCH_DEFENSE = {'name': "The French Defense",
                      'user_plays_white': False,
                      'variations':
                          {
                            'Winawer Variation': {0: 'e2e4', 1: 'e7e6', 2: 'd2d4', 3: 'd7d5', 4: 'b1d2', 5: 'f8b4'},
                            'Classical French' : {0: 'e2e4', 1: 'e7e6', 2: 'd2d4', 3: 'd7d5', 4: 'b1d2', 5: 'g8f6', 6: 'c1c5'}
                          }
                      }

THE_ENGLISH_OPENING = {'name': "The English Opening",
                      'user_plays_white': True,
                      'variations':
                          {
                            'Four Knights Variation': {0: 'c2c4', 1: 'e7e5', 2: 'b1c3', 3: 'g8f6', 4: 'g1f3', 5: 'b8c6'},
                            'Bremen System': {0: 'c2c4', 1: 'e7e5', 2: 'b1c3', 3: 'g8f6', 4: 'g2g3'}
                          }
                      }


OPENING_NUMBERS = {0: QUEENS_GAMBIT, 1: SCOTCH_GAME, 2: ITALIAN_GAME, 3: LONDON_SYSTEM, 4: VIENNA_GAME, 5: BLACKMAR_DIEMER_GAMBIT}
