import os
import tensorflow as tf
from tensorflow.python.keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
from keras import models
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout


print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
print(tf.test.is_gpu_available())
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
original_dataset_dir = r"image\train"
train_cats_dir = r"image\train\cat"
validation_cats_dir = r"image\validation\cat"
test_cats_dir = r"image\test\cat"
train_dogs_dir = r"image\train\dog"
validation_dogs_dir = r"image\validation\dog"
test_dogs_dir = r"image\test\dog"


#  将所有图像乘以1/255 缩放
train_datagen = ImageDataGenerator(rescale=1. / 255)
validation_datagen = ImageDataGenerator(rescale=1. / 255)

train_dir = r"image\train"
validation_dir = r"image\test"
train_generator = train_datagen.flow_from_directory(train_dir,
                                                    #  将所有图像的大小调整为150×150
                                                    target_size=(150, 150),
                                                    #  批量大小
                                                    batch_size=20,
                                                    #  需要用二进制标签
                                                    class_mode='binary')
validation_generator = validation_datagen.flow_from_directory(validation_dir,
                                                              target_size=(150, 150),
                                                              batch_size=20,
                                                              class_mode='binary')


#  训练数据增强
train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   #  表示图像随机旋转的角度范围
                                   rotation_range=40,
                                   #  图像在水平方向上平移的范围
                                   width_shift_range=0.2,
                                   #  图像在垂直方向上平移的范围
                                   height_shift_range=0.2,
                                   #  随机错切变换的角度
                                   shear_range=0.2,
                                   #  图像随机缩放的范围
                                   zoom_range=0.2,
                                   #  随机将一半图像水平翻转
                                   horizontal_flip=True)
#  验证数据不能增强
validation_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(train_dir,
                                                    #  将所有图像的大小调整为150×150
                                                    target_size=(150, 150),
                                                    #  批量大小
                                                    batch_size=32,
                                                    #  需要用二进制标签
                                                    class_mode='binary')
validation_generator = validation_datagen.flow_from_directory(validation_dir,
                                                              target_size=(150, 150),
                                                              batch_size=32,
                                                              class_mode='binary')


def model():
    model = models.Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(512, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    return model


#  初始化模型
model = model()
#  用于配置训练模型（优化器、目标函数、模型评估标准）
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#  查看各个层的信息
model.summary()
#  回调函数，在每个训练期之后保存模型
model_checkpoint = ModelCheckpoint('model.hdf5',  # 保存模型的路径
                                   monitor='loss',  # 被监测的数据
                                   verbose=1,  # 日志显示模式:0=>安静模式,1=>进度条,2=>每轮一行
                                   save_best_only=True)  # 若为True,最佳模型就不会被覆盖
#  用history接收返回值用于画loss/acc曲线
history = model.fit_generator(train_generator,
                              steps_per_epoch=100,
                              epochs=30,
                              validation_data=validation_generator,
                              validation_steps=50)
model.save('model.h5')

test_dir = r"image\test"
test_datagen = ImageDataGenerator(rescale=1. / 255)
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode='binary')

test_loss, test_acc = model.evaluate_generator(test_generator, steps=50)
print('test acc:', test_acc)
