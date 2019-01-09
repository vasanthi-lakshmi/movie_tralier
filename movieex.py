import movie2
import fresh_tomatoes
balabalamagadivoy=movie2.cinemaworld("balabalamagadivoy",
                                     "comedy movie",
                                     "https://naasongs.com/wp-content/uploads/2015/08/Bale-Bale-Magadivoy-2015.jpg",
                                     "https://www.youtube.com/watch?v=zUPx-Cj60Zk")
devadas=movie2.cinemaworld("devadas",
                           "comdey movie",
                           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJj9NBtfFQl-ymopnRl5I4lxVR4HbL-1hb3XD-UtrlEmrwddwn2g",
                           "https://www.youtube.com/watch?v=Q9EWF6fzg8o")
pokiri=movie2.cinemaworld("pokiri",
                          "love story",
                          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTx1s8B-NlGOCdSFP6A590TqeaTqtsjY9eP232bRJ9d5RgUQ0_A",
                          "https://www.youtube.com/watch?v=KPySnTIgOok")
eega=movie2.cinemaworld("Eega",
                        "animated movie",
                        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNRc4e3pvuyIozMGWtNCggBRs0PdqcP_QZRGjccFBA6TsAaaJ-Hg",
                        "https://www.youtube.com/watch?v=njEpusfnTyw")
sm=movie2.cinemaworld("S/oSatyamurthy",
                      "feel good movie",
                      "http://tollyrevenue.com/wp-content/uploads/2015/04/2nd-week-poster.jpg",
                      "https://www.youtube.com/watch?v=gycP7XRoTTs")
jawaan=movie2.cinemaworld("jawaan",
                          "solder life",
                          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5y8xroU_H4Efrfb_V6PIhKXF_AGZq7kCuoUh43e88azr0fCdp8w",
                          "https://www.youtube.com/watch?v=CvgUc5XiyfM")
temper=movie2.cinemaworld("Temper",
                           "actio film",
                           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGPGLHjW9731TwLV5YVUe685aYOOJ2SgvCHEm1-_uBAC_y5-cW",
                           "https://www.youtube.com/watch?v=oF3XBrcGYn8")
adirindi=movie2.cinemaworld("Adirindi",
                             "action thiller film",
                             "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3CV4z5-v8Yq0Tqu2CSTrmsZKpXAVwQxEhrndaFOiau_YZ5GD5Qw",
                             "https://www.youtube.com/watch?v=raSc82QlXVw")
shivalinga=movie2.cinemaworld("Shivalinga",
                               "horror movie",
                               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-XMYtoPW3UBd7jQwbfXxH4CVfLQ3ksAl6gRP0KS-vzGCtGPqOmw",
                               "https://www.youtube.com/watch?v=cwEe5nL3u9Q")
movies=[balabalamagadivoy,devadas,pokiri,eega,sm,jawaan,temper,adirindi,shivalinga]
fresh_tomatoes.open_movies_page(movies)
