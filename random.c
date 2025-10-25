#include <stdio.h>
#include <stdlib.h>

int predict(double access_count, double age, int dirty_bit, int reference_bit) {
    if (access_count <= 7961.0) {
        if (access_count <= 7953.5) {
            if (age <= 4.5) {
                if (access_count <= 7867.5) {
                    if (dirty_bit <= 0) {
                        if (access_count <= 887.5) {
                            if (access_count <= 334.0) {
                                if (age <= 2.5) {
                                    return 1;
                                } else {
                                    if (access_count <= 128.0) {
                                        if (access_count <= 97.5)
                                            return 0;
                                        else
                                            return 0;
                                    } else {
                                        if (access_count <= 275.5)
                                            return 1;
                                        else
                                            return 1;
                                    }
                                }
                            } else {
                                if (access_count <= 426.0) {
                                    if (age <= 3.5) {
                                        if (access_count <= 380.0)
                                            return 0;
                                        else
                                            return 0;
                                    } else {
                                        if (access_count <= 384.5)
                                            return 1;
                                        else
                                            return 1;
                                    }
                                } else {
                                    if (access_count <= 570.5)
                                        return 1;
                                    else
                                        return 0;
                                }
                            }
                        } else {
                            return 1; 
                        }
                    } else {
                        return 1;
                    }
                } else {
                    return 1;
                }
            } else {
                return 1;
            }
        } else {
            return 1;
        }
    } else {
        return 0;
    }
}

int main(int argc, char *argv[]) {
    if (argc != 5) {
        printf("Usage: %s <access_count> <age> <dirty_bit> <reference_bit>\n", argv[0]);
        return 1;
    }

    double access_count = atof(argv[1]);
    double age = atof(argv[2]);
    int dirty_bit = atoi(argv[3]);
    int reference_bit = atoi(argv[4]);

    int predicted_class = predict(access_count, age, dirty_bit, reference_bit);
    printf("Predicted Class: %d\n", predicted_class);

    return 0;
}
