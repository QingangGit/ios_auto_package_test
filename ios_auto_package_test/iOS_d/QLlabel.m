//
//  QLlabel.m
//  iOS_d
//
//  Created by qin on 2020/1/10.
//  Copyright © 2020年 Mplanet. All rights reserved.
//

#import "QLlabel.h"

@implementation QLlabel
@synthesize QLlabel_str;

-(void)self_show
{
    NSLog(@"QLlabel_show");
    QLlabel_str = @"";
}
- (void)category_test{
    NSLog(@"原始实例方法");
}
@end
