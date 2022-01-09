//
//  QLlabel+categ.m
//  iOS_d
//
//  Created by qin on 2020/1/10.
//  Copyright © 2020年 Mplanet. All rights reserved.
//

#import "QLlabel+categ.h"
#import <objc/runtime.h>

@implementation QLlabel (categ)
-(void)setT_s:(NSString *)t_s
{
    objc_setAssociatedObject(self, @"t_s", t_s, OBJC_ASSOCIATION_COPY);
}
-(NSString *)t_s
{
   return  objc_getAssociatedObject(self, @"t_s");
}
- (void)cate_show
{
    NSLog(@"cate_show");
}
- (void)category_test{
    NSLog(@"扩展类方法");
}

@end
