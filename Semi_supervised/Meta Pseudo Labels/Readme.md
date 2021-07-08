# Meta Pseudo Labels in Image classification

- Meta Pseudo Labels, a semi-supervised learning method that achieves a new state-of-the-art top-1 accuracy of 90.2% on ImageNet.(as of May 2021)
- Like Pseudo Labels, Meta Pseudo Labels has a teacher network to generate pseudo labels on unlabeled data to teach a student network. 
- However, unlike Pseudo Labels where the teacher is fixed, the teacher in Meta Pseudo Labels is constantly adapted by the feedback of the student's performance on the labeled dataset. As a result, the teacher generates better pseudo labels to teach the student. 


### Aim
 - [ ] Implement a Meta pseudo labels model
 - [ ] Train on CIFAR-10 and compare
 - [ ] 








### Other implementations 
- https://github.com/google-research/google-research/tree/master/meta_pseudo_labels
- https://github.com/sayakpaul/PAWS-TF
- https://paperswithcode.com/paper/meta-pseudo-labels#code
