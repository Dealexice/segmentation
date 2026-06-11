# YOLO Instance Segmentation Dataset Analysis Report

This report contains the object size analysis for each subset in the `archive/` directory. Bins are calculated based on two definitions: Bounding Box Dimension and Area (equivalent square side length).

---

## Part 1: Bounding Box Dimension-based Binning
*Bins are defined using the maximum bounding box side length: $\max(W, H)$ of each object.*
* **Small**: $\max(W, H) < 32\text{ px}$
* **Medium**: $32\text{ px} \le \max(W, H) \le 96\text{ px}$
* **Large**: $\max(W, H) > 96\text{ px}$

### Subfolder: `label masks`

| Body Part | Small (<32px) | Medium (32–96px) | Large (>96px) | Total |
| :--- | :--- | :--- | :--- | :--- |
| human bladder | 158 | 240 | 53 | 451 |
| human brain | 89 | 60 | 1 | 150 |
| human cardia | 325 | 345 | 91 | 761 |
| human cerebellum | 287 | 268 | 94 | 649 |
| human epiglottis | 167 | 62 | 29 | 258 |
| human jejunum | 277 | 570 | 180 | 1K |
| human kidney | 365 | 820 | 321 | 1.5K |
| human liver | 236 | 1.1K | 106 | 1.5K |
| human lung | 160 | 144 | 59 | 363 |
| human melanoma | 352 | 182 | 46 | 580 |
| human muscle | 35 | 92 | 8 | 135 |
| human oesophagus | 452 | 1.5K | 329 | 2.3K |
| human pancreas | 508 | 1.7K | 217 | 2.4K |
| human peritoneum | 125 | 321 | 63 | 509 |
| human placenta | 545 | 1.4K | 430 | 2.4K |
| human pylorus | 177 | 257 | 43 | 477 |
| human rectum | 106 | 247 | 35 | 388 |
| human salivory gland | 869 | 2.3K | 415 | 3.6K |
| human spleen | 1.7K | 1.5K | 631 | 3.8K |
| human testis | 146 | 230 | 29 | 405 |
| human tongue | 357 | 1.1K | 200 | 1.6K |
| human tonsile | 417 | 617 | 125 | 1.2K |
| human umbilical cord | 75 | 34 | 8 | 117 |
| mouse fat (white and brown)_subscapula | 283 | 269 | 4 | 556 |
| mouse femur | 360 | 380 | 172 | 912 |
| mouse heart | 418 | 315 | 9 | 742 |
| mouse kidney | 538 | 1.1K | 33 | 1.6K |
| mouse liver | 132 | 523 | 19 | 674 |
| mouse muscle_tibia | 58 | 111 | 3 | 172 |
| mouse spleen | 1.2K | 352 | 410 | 2K |
| mouse thymus | 754 | 530 | 372 | 1.7K |
| **Total (Archive)** | **11.7K** | **18.7K** | **4.5K** | **34.9K** |

### Subfolder: `label masks modify`

| Body Part | Small (<32px) | Medium (32–96px) | Large (>96px) | Total |
| :--- | :--- | :--- | :--- | :--- |
| human bladder | 124 | 274 | 2 | 400 |
| human brain | 85 | 61 | 0 | 146 |
| human cardia | 264 | 405 | 2 | 671 |
| human cerebellum | 224 | 325 | 0 | 549 |
| human epiglottis | 157 | 71 | 0 | 228 |
| human jejunum | 186 | 686 | 2 | 874 |
| human kidney | 169 | 1.1K | 0 | 1.2K |
| human liver | 162 | 1.2K | 2 | 1.4K |
| human lung | 139 | 169 | 10 | 318 |
| human melanoma | 335 | 195 | 3 | 533 |
| human muscle | 31 | 95 | 1 | 127 |
| human oesophagus | 267 | 1.8K | 19 | 2K |
| human pancreas | 306 | 1.9K | 18 | 2.2K |
| human peritoneum | 101 | 365 | 2 | 468 |
| human placenta | 219 | 1.7K | 1 | 2K |
| human pylorus | 153 | 284 | 4 | 441 |
| human rectum | 78 | 271 | 0 | 349 |
| human salivory gland | 540 | 2.6K | 5 | 3.1K |
| human spleen | 1.4K | 1.9K | 4 | 3.3K |
| human testis | 127 | 252 | 1 | 380 |
| human tongue | 210 | 1.2K | 5 | 1.4K |
| human tonsile | 349 | 696 | 0 | 1K |
| human umbilical cord | 71 | 35 | 0 | 106 |
| mouse fat (white and brown)_subscapula | 279 | 270 | 0 | 549 |
| mouse femur | 283 | 474 | 0 | 757 |
| mouse heart | 418 | 320 | 0 | 738 |
| mouse kidney | 524 | 1.1K | 0 | 1.6K |
| mouse liver | 107 | 539 | 0 | 646 |
| mouse muscle_tibia | 52 | 112 | 1 | 165 |
| mouse spleen | 1.2K | 431 | 0 | 1.7K |
| mouse thymus | 653 | 689 | 0 | 1.3K |
| **Total (Archive)** | **9.2K** | **21.4K** | **82** | **30.7K** |

### Subfolder: `mask binary`

| Body Part | Small (<32px) | Medium (32–96px) | Large (>96px) | Total |
| :--- | :--- | :--- | :--- | :--- |
| human bladder | 66 | 212 | 13 | 291 |
| human brain | 80 | 61 | 0 | 141 |
| human cardia | 142 | 313 | 20 | 475 |
| human cerebellum | 95 | 235 | 8 | 338 |
| human epiglottis | 68 | 83 | 3 | 154 |
| human jejunum | 95 | 319 | 51 | 465 |
| human kidney | 65 | 387 | 79 | 531 |
| human liver | 123 | 982 | 35 | 1.1K |
| human lung | 70 | 123 | 19 | 212 |
| human melanoma | 212 | 205 | 7 | 424 |
| human muscle | 23 | 80 | 4 | 107 |
| human oesophagus | 164 | 1.1K | 159 | 1.4K |
| human pancreas | 232 | 1.4K | 65 | 1.7K |
| human peritoneum | 48 | 301 | 11 | 360 |
| human placenta | 100 | 867 | 131 | 1.1K |
| human pylorus | 99 | 242 | 10 | 351 |
| human rectum | 39 | 220 | 6 | 265 |
| human salivory gland | 261 | 1.8K | 81 | 2.2K |
| human spleen | 465 | 1.4K | 76 | 1.9K |
| human testis | 83 | 237 | 4 | 324 |
| human tongue | 130 | 762 | 77 | 969 |
| human tonsile | 200 | 567 | 14 | 781 |
| human umbilical cord | 46 | 38 | 1 | 85 |
| mouse fat (white and brown)_subscapula | 271 | 262 | 1 | 534 |
| mouse femur | 80 | 241 | 36 | 357 |
| mouse heart | 404 | 314 | 2 | 720 |
| mouse kidney | 486 | 1K | 4 | 1.5K |
| mouse liver | 93 | 498 | 7 | 598 |
| mouse muscle_tibia | 48 | 106 | 2 | 156 |
| mouse spleen | 271 | 350 | 52 | 673 |
| mouse thymus | 134 | 297 | 49 | 480 |
| **Total (Archive)** | **4.7K** | **15K** | **1K** | **20.7K** |

### Subfolder: `mask binary without border`

| Body Part | Small (<32px) | Medium (32–96px) | Large (>96px) | Total |
| :--- | :--- | :--- | :--- | :--- |
| human bladder | 126 | 263 | 3 | 392 |
| human brain | 85 | 61 | 0 | 146 |
| human cardia | 273 | 391 | 2 | 666 |
| human cerebellum | 235 | 298 | 0 | 533 |
| human epiglottis | 140 | 74 | 0 | 214 |
| human jejunum | 186 | 637 | 7 | 830 |
| human kidney | 182 | 999 | 3 | 1.2K |
| human liver | 166 | 1.2K | 2 | 1.4K |
| human lung | 137 | 169 | 8 | 314 |
| human melanoma | 331 | 195 | 3 | 529 |
| human muscle | 30 | 94 | 1 | 125 |
| human oesophagus | 283 | 1.7K | 29 | 2K |
| human pancreas | 340 | 1.8K | 19 | 2.2K |
| human peritoneum | 108 | 361 | 2 | 471 |
| human placenta | 235 | 1.7K | 13 | 1.9K |
| human pylorus | 157 | 279 | 4 | 440 |
| human rectum | 87 | 263 | 0 | 350 |
| human salivory gland | 549 | 2.5K | 5 | 3.1K |
| human spleen | 1.4K | 1.7K | 5 | 3.2K |
| human testis | 131 | 244 | 2 | 377 |
| human tongue | 219 | 1.2K | 10 | 1.4K |
| human tonsile | 360 | 673 | 0 | 1K |
| human umbilical cord | 69 | 35 | 0 | 104 |
| mouse fat (white and brown)_subscapula | 282 | 267 | 0 | 549 |
| mouse femur | 275 | 442 | 0 | 717 |
| mouse heart | 416 | 321 | 0 | 737 |
| mouse kidney | 522 | 1.1K | 0 | 1.6K |
| mouse liver | 110 | 534 | 2 | 646 |
| mouse muscle_tibia | 53 | 111 | 1 | 165 |
| mouse spleen | 1.1K | 444 | 0 | 1.5K |
| mouse thymus | 618 | 616 | 0 | 1.2K |
| **Total (Archive)** | **9.2K** | **20.6K** | **121** | **29.9K** |

### Subfolder: `mask binary without border erode`

| Body Part | Small (<32px) | Medium (32–96px) | Large (>96px) | Total |
| :--- | :--- | :--- | :--- | :--- |
| human bladder | 169 | 229 | 1 | 399 |
| human brain | 90 | 56 | 0 | 146 |
| human cardia | 336 | 327 | 2 | 665 |
| human cerebellum | 347 | 191 | 0 | 538 |
| human epiglottis | 161 | 58 | 0 | 219 |
| human jejunum | 239 | 607 | 2 | 848 |
| human kidney | 269 | 930 | 0 | 1.2K |
| human liver | 223 | 1.1K | 2 | 1.4K |
| human lung | 160 | 148 | 8 | 316 |
| human melanoma | 363 | 164 | 2 | 529 |
| human muscle | 34 | 91 | 1 | 126 |
| human oesophagus | 363 | 1.6K | 21 | 2K |
| human pancreas | 463 | 1.7K | 16 | 2.2K |
| human peritoneum | 132 | 336 | 1 | 469 |
| human placenta | 320 | 1.6K | 7 | 1.9K |
| human pylorus | 184 | 257 | 3 | 444 |
| human rectum | 106 | 243 | 0 | 349 |
| human salivory gland | 729 | 2.4K | 3 | 3.1K |
| human spleen | 1.9K | 1.3K | 5 | 3.2K |
| human testis | 157 | 220 | 1 | 378 |
| human tongue | 279 | 1.1K | 4 | 1.4K |
| human tonsile | 462 | 576 | 0 | 1K |
| human umbilical cord | 74 | 32 | 0 | 106 |
| mouse fat (white and brown)_subscapula | 330 | 215 | 0 | 545 |
| mouse femur | 347 | 387 | 0 | 734 |
| mouse heart | 482 | 256 | 0 | 738 |
| mouse kidney | 679 | 916 | 0 | 1.6K |
| mouse liver | 137 | 506 | 1 | 644 |
| mouse muscle_tibia | 61 | 103 | 1 | 165 |
| mouse spleen | 1.3K | 273 | 0 | 1.6K |
| mouse thymus | 798 | 475 | 0 | 1.3K |
| **Total (Archive)** | **11.7K** | **18.5K** | **81** | **30.2K** |


---

## Part 2: Area-based Binning (Equivalent Square Side Length)
*Bins are defined using the object's mask area (pixel count):*
* **Small**: $\text{area} < 1024\text{ px}^2$ ($32^2$)
* **Medium**: $1024\text{ px}^2 \le \text{area} \le 9216\text{ px}^2$ (between $32^2$ and $96^2$)
* **Large**: $\text{area} > 9216\text{ px}^2$ ($96^2$)

### Subfolder: `label masks`

| Body Part | Small (<32px) | Medium (32–96px) | Large (>96px) | Total |
| :--- | :--- | :--- | :--- | :--- |
| human bladder | 366 | 85 | 0 | 451 |
| human brain | 122 | 28 | 0 | 150 |
| human cardia | 645 | 116 | 0 | 761 |
| human cerebellum | 604 | 45 | 0 | 649 |
| human epiglottis | 241 | 17 | 0 | 258 |
| human jejunum | 680 | 347 | 0 | 1K |
| human kidney | 989 | 517 | 0 | 1.5K |
| human liver | 617 | 850 | 0 | 1.5K |
| human lung | 309 | 54 | 0 | 363 |
| human melanoma | 526 | 54 | 0 | 580 |
| human muscle | 93 | 42 | 0 | 135 |
| human oesophagus | 1.2K | 1.2K | 0 | 2.3K |
| human pancreas | 1.5K | 968 | 0 | 2.4K |
| human peritoneum | 326 | 183 | 0 | 509 |
| human placenta | 1.4K | 1K | 0 | 2.4K |
| human pylorus | 382 | 95 | 0 | 477 |
| human rectum | 270 | 118 | 0 | 388 |
| human salivory gland | 2.3K | 1.2K | 0 | 3.6K |
| human spleen | 3.4K | 411 | 0 | 3.8K |
| human testis | 301 | 104 | 0 | 405 |
| human tongue | 969 | 649 | 0 | 1.6K |
| human tonsile | 968 | 191 | 0 | 1.2K |
| human umbilical cord | 114 | 3 | 0 | 117 |
| mouse fat (white and brown)_subscapula | 521 | 35 | 0 | 556 |
| mouse femur | 751 | 161 | 0 | 912 |
| mouse heart | 708 | 34 | 0 | 742 |
| mouse kidney | 1.2K | 381 | 0 | 1.6K |
| mouse liver | 303 | 371 | 0 | 674 |
| mouse muscle_tibia | 141 | 31 | 0 | 172 |
| mouse spleen | 2K | 6 | 0 | 2K |
| mouse thymus | 1.6K | 91 | 0 | 1.7K |
| **Total (Archive)** | **25.5K** | **9.4K** | **0** | **34.9K** |

### Subfolder: `label masks modify`

| Body Part | Small (<32px) | Medium (32–96px) | Large (>96px) | Total |
| :--- | :--- | :--- | :--- | :--- |
| human bladder | 309 | 91 | 0 | 400 |
| human brain | 118 | 28 | 0 | 146 |
| human cardia | 546 | 125 | 0 | 671 |
| human cerebellum | 508 | 41 | 0 | 549 |
| human epiglottis | 209 | 19 | 0 | 228 |
| human jejunum | 519 | 355 | 0 | 874 |
| human kidney | 673 | 549 | 0 | 1.2K |
| human liver | 514 | 856 | 0 | 1.4K |
| human lung | 259 | 59 | 0 | 318 |
| human melanoma | 481 | 52 | 0 | 533 |
| human muscle | 85 | 42 | 0 | 127 |
| human oesophagus | 869 | 1.2K | 0 | 2K |
| human pancreas | 1.2K | 1K | 0 | 2.2K |
| human peritoneum | 282 | 186 | 0 | 468 |
| human placenta | 835 | 1.1K | 0 | 2K |
| human pylorus | 347 | 94 | 0 | 441 |
| human rectum | 229 | 120 | 0 | 349 |
| human salivory gland | 1.8K | 1.3K | 0 | 3.1K |
| human spleen | 2.9K | 412 | 0 | 3.3K |
| human testis | 277 | 103 | 0 | 380 |
| human tongue | 746 | 669 | 0 | 1.4K |
| human tonsile | 846 | 199 | 0 | 1K |
| human umbilical cord | 103 | 3 | 0 | 106 |
| mouse fat (white and brown)_subscapula | 514 | 35 | 0 | 549 |
| mouse femur | 580 | 177 | 0 | 757 |
| mouse heart | 706 | 32 | 0 | 738 |
| mouse kidney | 1.2K | 386 | 0 | 1.6K |
| mouse liver | 275 | 371 | 0 | 646 |
| mouse muscle_tibia | 134 | 31 | 0 | 165 |
| mouse spleen | 1.6K | 9 | 0 | 1.7K |
| mouse thymus | 1.3K | 91 | 0 | 1.3K |
| **Total (Archive)** | **20.9K** | **9.7K** | **0** | **30.7K** |

### Subfolder: `mask binary`

| Body Part | Small (<32px) | Medium (32–96px) | Large (>96px) | Total |
| :--- | :--- | :--- | :--- | :--- |
| human bladder | 176 | 115 | 0 | 291 |
| human brain | 111 | 30 | 0 | 141 |
| human cardia | 315 | 159 | 1 | 475 |
| human cerebellum | 213 | 125 | 0 | 338 |
| human epiglottis | 126 | 28 | 0 | 154 |
| human jejunum | 230 | 221 | 14 | 465 |
| human kidney | 188 | 328 | 15 | 531 |
| human liver | 378 | 762 | 0 | 1.1K |
| human lung | 138 | 74 | 0 | 212 |
| human melanoma | 359 | 65 | 0 | 424 |
| human muscle | 63 | 44 | 0 | 107 |
| human oesophagus | 471 | 910 | 18 | 1.4K |
| human pancreas | 752 | 949 | 0 | 1.7K |
| human peritoneum | 156 | 204 | 0 | 360 |
| human placenta | 329 | 737 | 32 | 1.1K |
| human pylorus | 242 | 109 | 0 | 351 |
| human rectum | 136 | 129 | 0 | 265 |
| human salivory gland | 965 | 1.2K | 9 | 2.2K |
| human spleen | 1.1K | 762 | 9 | 1.9K |
| human testis | 204 | 120 | 0 | 324 |
| human tongue | 401 | 564 | 4 | 969 |
| human tonsile | 527 | 254 | 0 | 781 |
| human umbilical cord | 77 | 8 | 0 | 85 |
| mouse fat (white and brown)_subscapula | 493 | 41 | 0 | 534 |
| mouse femur | 168 | 186 | 3 | 357 |
| mouse heart | 680 | 40 | 0 | 720 |
| mouse kidney | 1.1K | 403 | 0 | 1.5K |
| mouse liver | 250 | 348 | 0 | 598 |
| mouse muscle_tibia | 123 | 33 | 0 | 156 |
| mouse spleen | 426 | 246 | 1 | 673 |
| mouse thymus | 267 | 200 | 13 | 480 |
| **Total (Archive)** | **11.2K** | **9.4K** | **119** | **20.7K** |

### Subfolder: `mask binary without border`

| Body Part | Small (<32px) | Medium (32–96px) | Large (>96px) | Total |
| :--- | :--- | :--- | :--- | :--- |
| human bladder | 301 | 91 | 0 | 392 |
| human brain | 118 | 28 | 0 | 146 |
| human cardia | 553 | 113 | 0 | 666 |
| human cerebellum | 485 | 48 | 0 | 533 |
| human epiglottis | 194 | 20 | 0 | 214 |
| human jejunum | 498 | 332 | 0 | 830 |
| human kidney | 697 | 487 | 0 | 1.2K |
| human liver | 517 | 835 | 0 | 1.4K |
| human lung | 259 | 55 | 0 | 314 |
| human melanoma | 477 | 52 | 0 | 529 |
| human muscle | 83 | 42 | 0 | 125 |
| human oesophagus | 872 | 1.1K | 0 | 2K |
| human pancreas | 1.2K | 968 | 0 | 2.2K |
| human peritoneum | 294 | 177 | 0 | 471 |
| human placenta | 875 | 1K | 0 | 1.9K |
| human pylorus | 348 | 92 | 0 | 440 |
| human rectum | 232 | 118 | 0 | 350 |
| human salivory gland | 1.8K | 1.2K | 0 | 3.1K |
| human spleen | 2.8K | 429 | 0 | 3.2K |
| human testis | 273 | 104 | 0 | 377 |
| human tongue | 757 | 641 | 0 | 1.4K |
| human tonsile | 851 | 182 | 0 | 1K |
| human umbilical cord | 101 | 3 | 0 | 104 |
| mouse fat (white and brown)_subscapula | 514 | 35 | 0 | 549 |
| mouse femur | 557 | 160 | 0 | 717 |
| mouse heart | 706 | 31 | 0 | 737 |
| mouse kidney | 1.2K | 386 | 0 | 1.6K |
| mouse liver | 280 | 366 | 0 | 646 |
| mouse muscle_tibia | 134 | 31 | 0 | 165 |
| mouse spleen | 1.5K | 54 | 0 | 1.5K |
| mouse thymus | 1.1K | 138 | 0 | 1.2K |
| **Total (Archive)** | **20.5K** | **9.4K** | **0** | **29.9K** |

### Subfolder: `mask binary without border erode`

| Body Part | Small (<32px) | Medium (32–96px) | Large (>96px) | Total |
| :--- | :--- | :--- | :--- | :--- |
| human bladder | 327 | 72 | 0 | 399 |
| human brain | 125 | 21 | 0 | 146 |
| human cardia | 578 | 87 | 0 | 665 |
| human cerebellum | 506 | 32 | 0 | 538 |
| human epiglottis | 209 | 10 | 0 | 219 |
| human jejunum | 583 | 265 | 0 | 848 |
| human kidney | 803 | 396 | 0 | 1.2K |
| human liver | 606 | 754 | 0 | 1.4K |
| human lung | 271 | 45 | 0 | 316 |
| human melanoma | 488 | 41 | 0 | 529 |
| human muscle | 93 | 33 | 0 | 126 |
| human oesophagus | 1K | 1K | 0 | 2K |
| human pancreas | 1.4K | 780 | 0 | 2.2K |
| human peritoneum | 317 | 152 | 0 | 469 |
| human placenta | 1K | 900 | 0 | 1.9K |
| human pylorus | 379 | 65 | 0 | 444 |
| human rectum | 255 | 94 | 0 | 349 |
| human salivory gland | 2.2K | 915 | 0 | 3.1K |
| human spleen | 2.9K | 287 | 0 | 3.2K |
| human testis | 294 | 84 | 0 | 378 |
| human tongue | 867 | 537 | 0 | 1.4K |
| human tonsile | 921 | 117 | 0 | 1K |
| human umbilical cord | 103 | 3 | 0 | 106 |
| mouse fat (white and brown)_subscapula | 526 | 19 | 0 | 545 |
| mouse femur | 613 | 121 | 0 | 734 |
| mouse heart | 717 | 21 | 0 | 738 |
| mouse kidney | 1.3K | 284 | 0 | 1.6K |
| mouse liver | 307 | 337 | 0 | 644 |
| mouse muscle_tibia | 138 | 27 | 0 | 165 |
| mouse spleen | 1.6K | 16 | 0 | 1.6K |
| mouse thymus | 1.2K | 83 | 0 | 1.3K |
| **Total (Archive)** | **22.6K** | **7.6K** | **0** | **30.2K** |

